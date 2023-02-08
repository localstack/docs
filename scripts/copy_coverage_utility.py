import csv
import os
import sys
from pathlib import Path
import json
from json import JSONDecodeError

DOCS_HEADER = """---
title: "LocalStack Coverage"
linkTitle: "LocalStack Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs in LocalStack
aliases:
  - /localstack/coverage/
hide_readingtime: true
---
\n\n
"""

TABLE_HEADER = """
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>"""



def create_metric_coverage_docs(file_name: str, metrics: dict):
    if os.path.exists(file_name):
        os.remove(file_name)

    output = DOCS_HEADER
    output += '<div class="coverage-report">\n\n'
    #header = f"<table>{TABLE_HEADER}\n"
    header = '<div id="service">'
    for service in sorted(metrics.keys()):
        output += f"## {service} ##\n\n"
        
        #output += "  <tbody>\n"
        details = metrics[service]

        implemented_ops = {
            operation[0]: operation[1]
            for operation in details.items()
            if operation[1]["implemented"]
        }

        not_implemented_ops = {
            operation[0]: operation[1]
            for operation in details.items()
            if not operation[1]["implemented"]
        }
        
        internal_tested = len([op for op, details in implemented_ops.items() if details.get("invoked", 0) > 0 and ("community-integration-test" in details.get("source",[]) or "pro-integration-test" in details.get("source",[])) ])
        all_tested = len([op for op, details in implemented_ops.items() if details.get("invoked", 0) > 0 and details.get("source",[])])
        aws_validated_count = len([op for op, details in implemented_ops.items() if details.get("aws_validated") or details.get("snapshot")])
        snapshot_count = len([op for op, details in implemented_ops.items() if details.get("snapshot")])
        snapshot_no_skip_count = len([op for op, details in implemented_ops.items() if details.get("snapshot") and not details.get("snapshot_skipped_paths")])

        output += f"{len(implemented_ops)} out of {len(details)} operations implemented.\n"
        output += header
        tested_internal_indicator = ' <a href="#misc" title="covered by our integration test suite">✨</a>'
        tested_external_indicator = ' <a href="#misc" title="covered by moto test suite">💫</a>'
        aws_validated = "☁✅"
        covered_internally = "✅"
        covered_externally = "♻"
        
       
        for operation in sorted(implemented_ops.keys()):
            op_details = implemented_ops.get(operation)
            detail_infos = ""
            if op_details.get("aws_validated") or op_details.get("snapshot"):
                detail_infos = f"""<a title="AWS validated">{aws_validated}</a>"""
            elif op_details.get("invoked", 0 ) > 0 and ("community-integration-test" in op_details.get("source") or "pro-integration-test" in op_details.get("source")):
                detail_infos = f"""<a title="Tested internally">{covered_internally}</a>"""
            elif op_details.get("invoked", 0 ) > 0:
                detail_infos = f"""<a title="Tested externally">{covered_externally}</a>"""

            tested = detail_infos
            pro_info = ""
            if implemented_ops.get(operation).get("pro"):
                pro_info = "Pro"
            else:
                pro_info = "Community"
            # output += (
            #     "    <tr>\n"
            #     f"      <td>{operation}{pro_info}{tested}</td>\n"
            #     '       <td style="text-align:right">✅</td>\n'
            #     "    </tr>\n"
            # )
            id = operation
            
            
            parameters = implemented_ops.get(operation).get("parameters")
            parameters.pop("_none_", "")
            if parameters:
                params = "<ul>\n"
                for p in parameters.keys():
                    params += f"  <li>{p}</li>\n"
                params += "</ul>"
            else:
                params = "only tested without parameters" if not parameters else ""
            


            # TODO terraform
            exceptions = implemented_ops.get(operation).get("errors")
            exceptions.pop("CommonServiceException", "")
            if exceptions:
                errors = "<ul>\n"
                for e in exceptions.keys():
                    errors += f"  <li>{e}</li>\n"
                errors += "</ul>"
            else:
                errors = "no exceptions tested"

            test_details_params = "no details available" if implemented_ops.get(operation).get("invoked", 0) == 0 else f"""<b>Parameters tested:</b> {params}"""
            test_details_exception = "" if implemented_ops.get(operation).get("invoked", 0) == 0 else f"""<b>Exceptions tested:</b> {errors}"""

            output += f"""<div class="card w-75">
            <div class="card-header" id="header_{operation}">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#{operation}" aria-controls="{operation}">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>{operation}</h5>
                    </div>
                    <div class="col text-right">{pro_info or "community"}
                    </div>
                     <div class="col text-right">{tested}
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="{operation}" class="collapse" aria-labelledby="header_{operation}" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">{test_details_params}</div>
                    <div class="col-sm">{test_details_exception}</div>
                </div>
                </div>
            </div>
            </div>
        </div>
        """
        #output += "  </tbody>\n"
        
        # if not_implemented_ops:
        #     output += (
        #         "  <tbody>"
        #         "    <tr>\n"
        #         f"""      <td><a data-toggle="collapse" href=".{service.lower()}-notimplemented">Show missing</a></td>\n"""
        #         '      <td style="text-align:right"></td>\n'
        #         "    </tr>\n"
        #         "  </tbody>\n"
        #         f"""  <tbody class="collapse {service.lower()}-notimplemented"> """
        #     )
        #     for operation in sorted(not_implemented_ops.keys()):
        #         output += (
        #             "    <tr>\n"
        #             f"      <td>{operation}</td>\n"
        #             '       <td style="text-align:right">-</td>\n'
        #             "    </tr>\n"
        #         )
        #     output += "  </tbody>\n"


        # output += " </table>\n\n"
        with open(file_name, "a") as fd:
            fd.write(f"{output}\n")
            output = ""

    with open(file_name, "a") as fd:
        fd.write(f"{output}\n")
        #fd.write(
        #    "## Misc ##\n\n" "Endpoints marked with ✨ are covered by our integration test suite.\n"
        #)
        #fd.write("The 💫 indicates that moto integration tests cover the endpoint, and run succesfully against LocalStack.")
        fd.write("\n\n</div>")




def main(path_to_implementation_details: str, path_to_raw_metrics: str):
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

    # now check the actual recorded test data and map the information
    recorded_metrics = aggregate_recorded_raw_data(
        base_dir=path_to_raw_metrics, service_dict=impl_details
    )

    # create the coverage-docs
    create_metric_coverage_docs(
        file_name=path_to_raw_metrics + "/coverage.md", metrics=recorded_metrics
    )


def _init_metric_recorder(service_dict: dict):
    """
    creates the base structure to collect raw data from the service_dict
    :param service_dict: 
    """
    recorder = {}
    for service, ops in service_dict.items():
        operations = {}
        for operation, details in ops.items():
            attributes = {
                "implemented": details["implemented"],
                "pro": details["pro"],
                "invoked": 0,
                "aws_validated": False,
                "snapshot": False,
                "parameters": {},
                "errors": {},
            }
            operations[operation] = attributes
        recorder[service] = operations
    return recorder


def aggregate_recorded_raw_data(base_dir: str, service_dict: dict):
    """
    collects all the raw metric data and maps them in a dict:
        { "service_name":
            {"operation-name":
                {"invoked": 0,
                "aws_validated": False,
                "snapshot": False,
                "parameters": {"param1": 0},
                "errors": {"InvokeException": 0},
                "tests": [],
                "source": [] },
            ....
            },
            ...
        }
    :param base_dir: directory where the raw-metrics csv-files are stored
    :param service_dict: dict 

    :returns: dict with details about invoked operations
    """
    recorded_data = _init_metric_recorder(service_dict)
    pathlist = Path(base_dir).rglob("*.csv")
    for path in pathlist:
        test_source = path.stem
        print(f"checking {str(path)}")
        with open(path, "r") as csv_obj:
            csv_dict_reader = csv.DictReader(csv_obj)
            for metric in csv_dict_reader:
                node_id = metric.get("node_id") or metric.get("test_node_id")

                # skip tests are marked as xfail
                if str(metric.get("xfail", "")).lower() == "true":
                    continue
                
                if metric.get("origin").lower() == "internal":
                    # exclude all internal service calls, those might be false positives for aws-validated tests
                    continue

                service = recorded_data.get(metric.get("service"))
                # some metrics (e.g. moto) could include tests for services, we do not support
                if not service:
                    print(f"---> service {metric.get('service')} was not found")
                    continue
                ops = service.get(metric.get("operation"))
                if not ops:
                    print(f"---> operation {metric.get('service')}.{metric.get('operation')} was not found")
                    continue

                errors = ops.setdefault("errors", {})
                if exception := metric.get("exception"):
                    if exception == "CommonServiceException":
                        try:
                            data = json.loads(metric.get("response_data","{}"))
                            exception = data.get("__type", exception)
                        except JSONDecodeError:
                            print(f"{metric.get('service')}: could not decode CommonServiceException details")
                            
                    errors[exception] = ops.get(exception, 0) + 1
                elif int(metric.get("response_code", -1)) >= 300:
                    # TODO we do not know the expected errors at this point
                    print(
                        f"Exception assumed for {metric.get('service')}.{metric.get('operation')}: code {metric.get('response_code')} {metric.get('response_data')}"
                    )
                    for expected_error in ops.get("errors", {}).keys():
                        if expected_error in metric.get("response_data"):
                            # assume we have a match
                            errors[expected_error] += 1
                            print(
                                f"Exception assumed for {metric.service}.{metric.operation}: code {metric.response_code}"
                            )
                            break

                ops["invoked"] += 1
                if str(metric.get("snapshot", "false")).lower() == "true":
                    if ops.get("snapshot") == True:
                        # only update snapshot_skipped_paths if necessary (we prefer the test record where nothing was skipped)
                        ops["snapshot_skipped_paths"] = "" if metric.get("snapshot_skipped_paths", "") else ops.get("snapshot_skipped_paths", "") 
                    else:
                        ops["snapshot"] = True  # TODO snapshot currently includes also "skip_verify"
                        ops["snapshot_skipped_paths"] = metric.get("snapshot_skipped_paths", "") 

                if str(metric.get("aws_validated", "false")).lower() == "true":
                    ops["aws_validated"] = True
                if not metric.get("parameters"):
                    params = ops.setdefault("parameters", {})
                    params["_none_"] = params.get("_none_", 0) + 1
                else:
                    for p in metric.get("parameters").split(","):
                        ops["parameters"][p] = ops["parameters"].setdefault(p, 0) + 1

                source_list = ops.setdefault("source", [])
                if test_source not in source_list:
                    source_list.append(test_source)

                test_list = ops.setdefault("tests", [])

                test_node_id = f"{test_source}_{node_id}"
                if test_node_id not in test_list:
                    test_list.append(test_node_id)

    return recorded_data


def print_usage():
    print("missing arguments")
    print(
        "usage: python coverage_docs_utility.py <dir-to-implementation-details> <dir-to-raw-csv-metric>"
    )


if __name__ == "__main__":
    if len(sys.argv) != 3 or not Path(sys.argv[1]).is_dir() or not Path(sys.argv[2]).is_dir():
        print_usage()
    else:
        main(sys.argv[1], sys.argv[2])
