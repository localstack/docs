import os
from io import BytesIO
import json
import notion_client as n_client
import frontmatter
from notion.catalog import PersistenceCatalog

token = os.getenv("NOTION_TOKEN")
markdown_path = "../../content/en/user-guide/aws"
persistence_path = "../../data/persistence"
persistence_data = os.path.join(persistence_path, "coverage.json")

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
    return dict(sorted(statuses.items()))


def update_coverage_data():
    if not token:
        print("Aborting, please provide a NOTION_TOKEN in the env") 
    statuses = collect_status()
    if not os.path.exists(persistence_path):
        os.mkdir(persistence_path)
    
    with open(persistence_data, 'w') as f:
        json.dump(statuses, f, indent=2)
    
    
def update_frontmatter():
    """Updates the frontmatter of the service page in the user guide Markdown file"""
    with open(persistence_data, 'r') as f:
        content = f.read()
    statuses = json.loads(content)
    for service, values in statuses.items():
        _path = os.path.join(markdown_path, service, "index.md")
        if not os.path.exists(_path):
            print(f" Can't find index.md file for {service}")
            continue
         
        # open the markdown file and read the content
        content = frontmatter.load(_path)
        desc = content.metadata["description"]
        content.metadata["description"] = desc.strip()
        content.metadata["persistence"] = values.get("support", "unknown")
        frontmatter.dump(content, _path)


if __name__ == "__main__":
    update_coverage_data()
    update_frontmatter()

