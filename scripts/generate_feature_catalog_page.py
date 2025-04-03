import os
import sys
from pathlib import Path

import yaml

DEFAULT_STATUS = 'not supported'
DEFAULT_EMULATION_LEVEL = 'CRUD'
FEATURES_FILE_NAME='features.yml'

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
|-------------------|----------------|-----------------|--------------------------|"""

class FeatureCatalogMarkdownGenerator:
    md_content = [MD_FILE_HEADER]

    def __init__(self, file_path: str):
        self.file_path = file_path
        pass

    def add_service_section(self, feature_file_content: str):
        service_name = feature_file_content.get('name')
        emulation_level = feature_file_content.get('emulation_level', DEFAULT_EMULATION_LEVEL)
        self.md_content.append(f"| **{service_name}** | [Details 🔍] | {emulation_level} | |")

    def add_features_rows(self, feature_file_content: str):
        for feature in feature_file_content.get('features', []):
            feature_name = feature.get('name', '')
            documentation_page = feature.get('documentation_page')
            if documentation_page:
                feature_name = f'[{feature_name}]({documentation_page})'
            status = feature.get('status', DEFAULT_STATUS)

            limitations = feature.get('limitations', [])
            limitations_md = '\n '.join(limitations) if limitations else ''

            self.md_content.append(f"| {feature_name} | {status} |  | {limitations_md} |")

    def generate_file(self):
        try:
            with open(self.file_path, "w") as feature_coverage_md_file:
                feature_coverage_md_file.writelines(s + '\n' for s in self.md_content)
        except Exception as e:
            print(f"Error writing to file: {e}")
            sys.exit(1)

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

def get_service_path_to_abs_community_ext_paths(community_files_path: str, ext_files_path: str) -> dict[str, (str, str)]:
    relative_to_abs_paths = {}
    for community_abs_path in Path(community_files_path).rglob(FEATURES_FILE_NAME):
        rel_path = str(community_abs_path.relative_to(community_files_path))
        relative_to_abs_paths[rel_path] = (community_abs_path, None)

    for abs_path_ext in Path(ext_files_path).rglob(FEATURES_FILE_NAME):
        rel_path = str(abs_path_ext.relative_to(ext_files_path))
        if rel_path in relative_to_abs_paths:
            community_abs_path, _ = relative_to_abs_paths[rel_path]
            relative_to_abs_paths[rel_path] = (community_abs_path, abs_path_ext)
        else:
            relative_to_abs_paths[rel_path] = (None, abs_path_ext)
    return relative_to_abs_paths

def main():
    community_feature_files_path = os.getenv('PATH_FEATURE_FILES_COMMUNITY')
    ext_feature_files_path = os.getenv('PATH_FEATURE_FILES_EXT')
    feature_catalog_md_file_path = os.getenv('PATH_FEATURE_CATALOG_MD')

    service_path_to_abs_paths = get_service_path_to_abs_community_ext_paths(community_feature_files_path, ext_feature_files_path)
    md_generator = FeatureCatalogMarkdownGenerator(feature_catalog_md_file_path)

    for service_name in sorted(service_path_to_abs_paths):
        abs_path_community, abs_path_ext = service_path_to_abs_paths.get(service_name)
        service_definition_created = False
        if abs_path_community:
            feature_file_community = load_yaml_file(abs_path_community)
            md_generator.add_service_section(feature_file_community)
            service_definition_created = True
            md_generator.add_features_rows(feature_file_community)
        if abs_path_ext:
            feature_file_ext = load_yaml_file(abs_path_ext)
            if not service_definition_created:
                md_generator.add_service_section(feature_file_community)
            md_generator.add_features_rows(feature_file_ext)
    md_generator.generate_file()

if __name__ == "__main__":
    main()
