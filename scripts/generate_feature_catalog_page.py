import os
import sys

import yaml

DEFAULT_STATUS = 'not supported'
DEFAULT_EMULATION_LEVEL = 'CRUD'

MD_FILE_HEADER = """---
title: "AWS Service Feature Coverage"
linkTitle: "⭐ Feature Coverage"
weight: 1
description: >
  Overview of the implemented AWS APIs and their level of parity with the AWS cloud
aliases:
  - /localstack/coverage/
  - /aws/feature-coverage/
hide_readingtime: true
---


## Emulation Levels

* CRUD: The service accepts requests and returns proper (potentially static) responses.
  No additional business logic besides storing entities.
* Emulated: The service imitates the functionality, including synchronous and asynchronous business logic operating on service entities.

| Service / Feature | Implementation status | Emulation Level | Limitations |
|-------------------|----------------|-----------------|--------------------------|
"""


def yml_to_md_table(yml_content):
    service_name = yml_content.get('name')
    emulation_level = yml_content.get('emulation_level', DEFAULT_EMULATION_LEVEL)
    md_table = f"| **{service_name}** | [Details 🔍] | {emulation_level} | |\n"

    # Add features
    for feature in yml_content.get('features', []):
        feature_name = feature.get('name', '')
        documentation_page = feature.get('documentation_page')
        if documentation_page:
            feature_name = f'[{feature_name}]({documentation_page})'
        status = feature.get('status', DEFAULT_STATUS)

        # Get limitations
        limitations = feature.get('limitations', [])
        limitations_md = '\n '.join(limitations) if limitations else ''

        md_table += f"| {feature_name} | {status} | {emulation_level} | {limitations_md} |\n"

    return md_table

def load_yaml_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"YAML file not found: {file_path}")
        sys.exit(1)

def main():
    changed_features_files = os.getenv('ALL_CHANGED_FEATURES_FILES').split(',')
    try:
        with open("new-feature-coverage.md", "w") as feature_coverage_md_file:
            feature_coverage_md_file.write(MD_FILE_HEADER)

            for file_path in changed_features_files:
                features_file = load_yaml_file(file_path)
                features_md = yml_to_md_table(features_file)
                feature_coverage_md_file.write(features_md)
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
