import csv
import os
import sys
from pathlib import Path
import json
from json import JSONDecodeError
from pathlib import Path
import shutil
from operator import itemgetter

DOCS_MD = """---
title: "LocalStack Coverage for {service}"
linkTitle: "LocalStack Coverage {service}"
description: >
  Overview of the implemented AWS APIs in {service}
hide_readingtime: true
---

{{{{< localstack_coverage service="{service}" >}}}}

"""

def create_markdown_files_for_services(target_dir: str, services: list[str], delete_if_exists: bool=False):   
    for service in services:

        dirpath = Path(target_dir).joinpath(f"coverage_{service}")
        if delete_if_exists:
            if dirpath.exists() and dirpath.is_dir():
                shutil.rmtree(dirpath)
        
        dirpath.mkdir(parents=True, exist_ok=True)

        file_name = dirpath.joinpath("index.md")
        with open(file_name, "w") as fd:
            fd.write(DOCS_MD.format(service=service))

        print(f"--> created markdown: {file_name}")


def create_data_templates_for_service(target_dir: str, metrics: dict, service: str, delete_if_exists: bool=False):
    output = {}
    details = metrics.pop("details", {})
    operations = []
    for key, value in metrics.items():
        operations.append({key: value})
    
    output["service"] = service
    output["operations"] = operations

    # sort the details
    for op_details, params in details.items():
        # alphabetically by parameters
        details[op_details] = dict(sorted(params.items()))
        for param, test_suites in details[op_details].items():
            # alphabetically by test-suite (ls-community/ls-pro)
            details[op_details][param] = dict(sorted(test_suites.items()))
            for test_suite, test_list in details[op_details][param].items():
                # by test details e.g. first response code then node_id
                details[op_details][param][test_suite] = sorted(test_list, key=itemgetter('response', 'node_id'))

    # sort alphabetically by operation-name
    output["details"] = dict(sorted(details.items()))
    
    # TODO add long_name?
    # output["long_name"] = lookup_service_long_name(service)

    # write data-template file
    dirpath = Path(target_dir)
    if delete_if_exists:
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)
    
    dirpath.mkdir(parents=True, exist_ok=True)

    file_name = dirpath.joinpath(f"{service}.json")
    with open(file_name, "w") as fd:
        json.dump(output, fd, indent=2)

    print(f"--> created data-template: {file_name}")

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
    
    for service in services:
        # now check the actual recorded test data and map the information
        recorded_metrics = aggregate_recorded_raw_data(
            base_dir=path_to_raw_metrics, operations=impl_details.get(service), service_of_interest=service
        )
        # TODO special handling for rds/neptune/docdb
        if service in ["neptun", "docdb"]:
            service = "rds"
        create_data_templates_for_service(target_dir + "/data", recorded_metrics, service)


def _init_metric_recorder(operations_dict: dict):
    """
    creates the base structure to collect raw data from the service_dict
    :param operations_dict: 
    """
    operations = {}
    for operation, details in operations_dict.items():
        availability = "pro" if details["pro"] else "community"
        if not details["implemented"]:
            availability = ""
        op_attributes = {
            "implemented": details["implemented"],
            "availability": availability,
            "internal_test_suite": False,
            "external_test_suite": False,
            "aws_validated": False,
            "snapshot_tested": False,
            "snapshot_skipped": "",
        }
        operations[operation] = op_attributes

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

                # skip tests are marked as xfail
                if str(metric.get("xfail", "")).lower() == "true":
                    continue
                
                
                op_name = metric.get("operation")
                op_record = recorded_data.get(op_name)
                if not op_record:
                    print(f"---> operation {metric.get('service')}.{metric.get('operation')} was not found")
                    continue
                
                internal_test = False
                external_test = False
                
                if test_source.startswith("community"):
                    test_node_origin = "LocalStack Community"
                    internal_test = True
                    source = "ls_community"
                elif test_source.startswith("pro"):
                    test_node_origin = "LocalStack Pro"
                    internal_test = True
                    source = "ls_pro"
                else:
                    external_test = True
                
                if internal_test and not op_record.get("internal_test_suite"):
                    op_record["internal_test_suite"] = True
                if external_test and not op_record.get("external_test_suite"):
                    op_record["external_test_suite"] = True
                
                aws_validated = str(metric.get("aws_validated", "false")).lower() == "true"

                # snapshot_tested is set if the test uses the snapshot-fixture + does not skip everything (pytest.marker.skip_snapshot_verify)
                snapshot_tested = (str(metric.get("snapshot", "false")).lower() == "true" 
                                    and metric.get("snapshot_skipped_paths", "") != 'all')
                
                if snapshot_tested and not aws_validated:
                    # the test did not have the marker aws_validated, but as it is snapshot_tested we can assume aws-validation
                    aws_validated = True
                
                if not op_record.get("snapshot_tested") and snapshot_tested:
                    op_record["snapshot_tested"] = True
                    op_record["aws_validated"] = True
                
                if not op_record.get("aws_validated") and aws_validated:
                    op_record["aws_validated"] = True
                
                # test details currently only considered for internal
                # TODO might change when we include terraform test results
                if not internal_test:
                    continue
                

                details = recorded_data.setdefault("details", {})
                details_tests = details.setdefault(op_name, {})
                
                params = metric.get("parameters", "None").split(",")
                params.sort()
                parameters = ", ".join(params)
                if not parameters:
                    parameters = "without any parameters"

                param_test_details = details_tests.setdefault(parameters, {})
                test_list = param_test_details.setdefault(source, [])

                node_id = metric.get("node_id") or metric.get("test_node_id")
                if param_exception := metric.get("exception", ""):
                    if param_exception == "CommonServiceException":
                        try:
                            data = json.loads(metric.get("response_data","{}"))
                            param_exception = data.get("__type", param_exception)
                        except JSONDecodeError:
                            print(f"{metric.get('service')}: could not decode CommonServiceException details ({param_exception})")
            
                test_detail = {
                    "node_id": f"{test_node_origin}: {node_id}",
                    "test": node_id.split("::")[-1],
                    "response": metric.get("response_code", -1),
                    "error": param_exception,
                    "snapshot_skipped": metric.get("snapshot_skipped_paths", ""),
                    "aws_validated": aws_validated,
                    "snapshot_tested": snapshot_tested,
                    "origin": metric.get("origin", "")
                }

                test_list.append(test_detail)

                # TODO do we still need counter to keep track of #invoked? 
                # ops["invoked"] += 1                         

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
