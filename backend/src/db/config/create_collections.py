from pymongo import ASCENDING, IndexModel
from .item_collection_example import ITEM_COLLECTION_EXAMPLE
from .category_collection_example import CATEGORY_COLLECTION_EXAMPLE
from db.schemas.item_schema import ItemSchema
from db.serializers.schema_serializer import schema_serializer


def create_collections(database):
    """
    Create all collections and insert the example data.

    """

    if 'itens' not in database.db.list_collection_names():
        collections = ['itens']

        for collection in collections:
            schema = ItemSchema()
            database.create_collection(
                collection,
                indexes=[IndexModel([("id", ASCENDING)], unique=True)],
                validation_schema=schema_serializer(schema.get())
            )

        for item in ITEM_COLLECTION_EXAMPLE:
            database.insert_item('itens', item)

    if 'categories' not in database.db.list_collection_names():
        collections = ['categories']

        for collection in collections:
            schema = ItemSchema()
            database.create_collection(
                collection,
                indexes=[IndexModel([("id", ASCENDING)], unique=True)],
                validation_schema=schema_serializer(schema.get())
            )

        for category in CATEGORY_COLLECTION_EXAMPLE:
            database.insert_item('itens', item)
