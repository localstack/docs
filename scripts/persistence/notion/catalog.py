"""Models for the notion service catalog https://www.notion.so/localstack/3c0f615e7ffc4ae2a034f1ed9c444bd2"""

from notion_client import Client as NotionClient

from notion_objects import (
    Page,
    TitlePlainText,
    Status,
    Database,
    Checkbox,
    PeopleProperty,
    Text
)

DEFAULT_CATALOG_DATABASE_ID = "3c0f615e7ffc4ae2a034f1ed9c444bd2"


class PersistenceServiceItem(Page):
    name = TitlePlainText("Name")
    status = Status("Persistence")
    has_test = Checkbox("Persistence Tests")
    primary_owner = PeopleProperty("Primary Owner")
    secondary_owner = PeopleProperty("Secondary Owner(s)")
    limitations = Text("Limitations (synced with docs)")
    exclude = Checkbox("Exclude from docs")


class PersistenceCatalog(Database[PersistenceServiceItem]):
    def __init__(self, notion_client: NotionClient, database_id: str | None = None):
        super().__init__(PersistenceServiceItem, database_id or DEFAULT_CATALOG_DATABASE_ID, notion_client)
