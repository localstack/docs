import os
import json
import notion_client as n_client
from notion.catalog import PersistenceCatalog

token = os.getenv("NOTION_TOKEN")
coverage_path = "../../data/coverage"


def collect_status() -> dict:
    """Reads the catalog on Notion and returns the status of persistence for each service"""
    notion_client = n_client.Client(auth=token)
    
    catalog_db = PersistenceCatalog(notion_client=notion_client)
    statuses = {}
    for item in catalog_db:
        service = item.name.replace('_', '-')
        status = item.status.lower()
        statuses[service] = {
            "support": status,
            "test_suite": item.has_test or False
        }
    return statuses


def update_coverage_data():
    if not token:
        print("Aborting, please provide a NOTION_TOKEN in the env") 
    statuses = collect_status()
    for service, status in statuses.items():
        f = os.path.join(coverage_path, f"{service}.json")
        if not os.path.exists(f):
            print(f"coverage file for {service} not found; skipping")
            continue
        print(f"Updating persistence coverage data for {service}")
        with open(f, 'r') as r_file:
            content = json.load(r_file)

        content.setdefault("feature_support", {"persistence": status})
        with open(f, 'w') as w_file:
            json.dump(content, w_file, indent=2)


if __name__ == "__main__":
    update_coverage_data()
