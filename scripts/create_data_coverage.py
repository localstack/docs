import csv
import os
import sys
from pathlib import Path
import json
from json import JSONDecodeError
from pathlib import Path
import shutil

DOCS_MD = """---
title: "LocalStack Coverage for {service}"
linkTitle: "LocalStack Coverage {service}"
description: >
  Overview of the implemented AWS APIs in {service}
hide_readingtime: true
---

{{< localstack_coverage service="{service}" >}}

"""

def create_markdown_files_for_services(target_dir: str, services: list[str], delete_if_exists=False):   
    for service in services:
        #output += f"## {service} ##\n\n"
        if service != 'acm':
            continue
        
        dirpath = Path(target_dir).joinpath(service)
        if delete_if_exists:
            if dirpath.exists() and dirpath.is_dir():
                shutil.rmtree(dirpath)
        
        dirpath.mkdir(parents=True, exist_ok=True)

        file_name = dirpath.joinpath("index.md")
        with open(file_name, "w") as fd:
            fd.write(DOCS_MD.format(service=service))

        print(f"--> created markdown: {file_name}")


def create_data_templates_for_service(target_dir: str, metrics: dict):
    pass

def main(path_to_implementation_details: str, path_to_raw_metrics: str, target_dir: str):
    impl_details = {}
    # read the implementation-details for pro + community first and generate a dict
    # with information about all services and operation, and indicator if those are implemented, and avaiable only in pro:
    # {"service_name": 
    #   {
    #       "operation_name": {"implemented": True, "pro": False}
    #   }
    # }
    with open(
        f"{path_to_implementation_details}/pro/implementation_coverage_full.csv", mode="r"
    ) as file:
        # check pro implementation details first
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            service = impl_details.setdefault(row["service"], {})
            service[row["operation"]] = {
                "implemented": True if row["is_implemented"] == "True" else False,
                "pro": True,
            }
    with open(
        f"{path_to_implementation_details}/community/implementation_coverage_full.csv", mode="r"
    ) as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            service = impl_details.setdefault(row["service"], {})
            # update all operations that are available in community
            if row["is_implemented"] == "True":
                service[row["operation"]]["pro"] = False 



    # create the coverage-docs
    services = sorted(impl_details.keys())
    create_markdown_files_for_services(
        target_dir=target_dir + "/md", services=services
    )

    for service in ["acm"]:#services:
        # now check the actual recorded test data and map the information
        # TODO special handling for rds/neptune/docdb
        recorded_metrics = aggregate_recorded_raw_data(
            base_dir=path_to_raw_metrics, operations=impl_details.get(service), service_of_interest=service
        )
        create_data_templates_for_service(target_dir + "/data", recorded_metrics)



def _init_metric_recorder(operations_dict: dict):
    """
    creates the base structure to collect raw data from the service_dict
    :param operations_dict: 
    """
    operations = {}
    for operation, details in operations_dict.items():
        attributes = {
            "implemented": details["implemented"],
            "pro": details["pro"],
            "invoked": 0,
            "aws_validated": False,
            "snapshot": False,
            "parameters": {},
            "errors": {},
            "origin": ""
        }
        operations[operation] = attributes
    return operations


def aggregate_recorded_raw_data(base_dir: str, operations: dict, service_of_interest: str):
    """
    collects all the raw metric data and maps them in a dict:
            {"operation-name":
                {"invoked": 0,
                "aws_validated": False,
                "snapshot": False,
                "parameter_combination": {"param_identifier": {"params":[param1, param2],"test": {"node_id": {"snapshot": True, "skipped_path": "all"}},"response":200, "error": "exception")},
                "source": [] },
            ....
            }
    :param base_dir: directory where the raw-metrics csv-files are stored
    :param operations: dict 
    :param service: service of interest
    :returns: dict with details about invoked operations
    """
    # TODO contains internal + external
    recorded_data = _init_metric_recorder(operations)
    pathlist = Path(base_dir).rglob("*.csv")
    for path in pathlist:
        test_source = path.stem
        print(f"checking {str(path)}")
        with open(path, "r") as csv_obj:
            csv_dict_reader = csv.DictReader(csv_obj)
            for metric in csv_dict_reader:
                service = metric.get("service")
                if service != service_of_interest:
                    continue

                node_id = metric.get("node_id") or metric.get("test_node_id")
                # skip tests are marked as xfail
                if str(metric.get("xfail", "")).lower() == "true":
                    continue
                
                # TODO skipping "internal" seems to lower the coverage now, because some tests use e.g. cfn other implicit calls
                # to verify behavior -> takle this issue in the next iteration
                #if metric.get("origin").lower() == "internal":
                #    # exclude all internal service calls, those might be false positives for aws-validated tests
                #    continue

                # some metrics (e.g. moto) could include tests for services, we do not support

                ops = recorded_data.get(metric.get("operation"))
                if not ops:
                    print(f"---> operation {metric.get('service')}.{metric.get('operation')} was not found")
                    continue
                
                ops["invoked"] += 1
                if param_exception := metric.get("exception", ""):
                    if param_exception == "CommonServiceException":
                        try:
                            data = json.loads(metric.get("response_data","{}"))
                            param_exception = data.get("__type", param_exception)
                        except JSONDecodeError:
                            print(f"{metric.get('service')}: could not decode CommonServiceException details")
                            

                if str(metric.get("snapshot", "false")).lower() == "true":
                    if ops.get("snapshot") == True:
                        # only update snapshot_skipped_paths if necessary (we prefer the test record where nothing was skipped)
                        ops["snapshot_skipped_paths"] = "" if metric.get("snapshot_skipped_paths", "") else ops.get("snapshot_skipped_paths", "") 
                    else:
                        ops["snapshot"] = True  # TODO snapshot currently includes also "skip_verify"
                        ops["snapshot_skipped_paths"] = metric.get("snapshot_skipped_paths", "") 

                if str(metric.get("aws_validated", "false")).lower() == "true":
                    ops["aws_validated"] = True

                parameter_combination = ops.setdefault("parameter_combination", {})
                test_node_origin = ""
                if test_source.startswith("community"):
                    test_node_origin = "LocalStack Community"
                elif test_source.startswith("pro"):
                    test_node_origin = "LocalStack Pro"
                elif test_source.startswith("moto"):
                    test_node_origin = "Moto"


                params = metric.get("parameters", "None").split(",")
                params.sort()

                parameters = ", ".join(params)
                response_code = int(metric.get("response_code", -1))


                param_details = parameter_combination.setdefault(parameters, {})
                if not param_details:
                    param_details["params"] = parameters

                node_ids = param_details.setdefault("tests", {})
                
                test_node_id = f"{test_node_origin}: {node_id}"
                # remove parametrized info from node id, as it will have the same attributes
                #cur_node_id_simple = test_node_id.split("[")[0]
                node_ids[test_node_id] = {
                    "source": test_node_origin,
                    "snapshot": metric.get("snapshot", "false").lower() == "true",
                    "skipped_path": metric.get("snapshot_skipped_paths", ""),
                    "aws_validated": str(metric.get("aws_validated", "false")).lower() == "true",
                    "response": response_code,
                    "error":  param_exception,
                    "origin": metric.get("origin", "")}
                
                # "parameter_combination": {"param_identifier": {"params":"param1, param2","tests": {"node_id": {"snapshot": True, "skipped_path": "all","response":200, "error": "exception"}}}


                source_list = ops.setdefault("source", [])
                if test_source not in source_list:
                    source_list.append(test_source)

    return recorded_data


def print_usage():
    print("missing arguments")
    print(
        "usage: python create_data_coverage.py <dir-to-implementation-details> <dir-to-raw-csv-metric> <target-dir>"
    )


if __name__ == "__main__":
    if len(sys.argv) != 4 or not Path(sys.argv[1]).is_dir() or not Path(sys.argv[2]).is_dir():
        print_usage()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
