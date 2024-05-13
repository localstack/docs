import os
from io import BytesIO
import json
import notion_client as n_client
import frontmatter
from notion.catalog import PersistenceCatalog

token = os.getenv("NOTION_TOKEN")
coverage_path = "../../data/coverage"
markdown_path = "../../content/en/user-guide/aws"


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
    """This function augments the coverage data files (one per service) by adding information
    about persistence support; such data is obtained from the persistence catalog on Notion"""
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


def update_frontmatter():
    """Updates the frontmatter of the service page in the user guide Markdown file"""
    coverage_files = [_f for _f in os.listdir(coverage_path) if _f.endswith("json")]
    if not coverage_files:
        print("Can't find any coverage file; something went wrong; abort")
    for cov_file in coverage_files:
        service = cov_file.split('.')[0]
        _path = os.path.join(markdown_path, service, "index.md")
        if not os.path.exists(_path):
            print(f" Can't find index.md file for {service}")
            continue
        
        # read the status of persistence from the coverage JSON data
        with open(os.path.join(coverage_path, cov_file), 'r') as f:
            data = json.loads(f.read())
        status = data.get("feature_support", {}).get("persistence", {}).get("status", "unknown")
     
        # open the markdown file and read the content
        content = frontmatter.load(_path)
        content.metadata["persistence"] = status
        frontmatter.dump(content, _path)


if __name__ == "__main__":
    update_coverage_data()
    update_frontmatter()

