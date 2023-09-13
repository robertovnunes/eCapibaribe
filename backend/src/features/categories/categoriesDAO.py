import json as json
from typing import Union
from logging import INFO, WARNING, getLogger

from pydantic import BaseModel

CATEGORY_DATABASE_FILE = "src/features/categories/data/categories.json"

logger = getLogger('uvicorn')


class Category(BaseModel):
    id: Union[str, None] = None
    name: str
    description: str
    image: str
    keywords: list
    items: list


def get_categories_db():
    with open(CATEGORY_DATABASE_FILE) as c:
        cdb = json.load(c)
    return cdb


def write_categories_db(cdb):
    with open(CATEGORY_DATABASE_FILE, 'w') as c:
        json.dump(cdb, c)


class database:

    @staticmethod
    def get_all_categories() -> list:
        """
        Get all itens from a collection

        Parameters:
        - collection_name: str
            The name of the collection

        Returns:
        - list
            A list of all itens in the collection

        """
        cdb = get_categories_db()
        return cdb

    @staticmethod
    def get_category(category_id: str) -> Category:
        """
        Retrieve an item by its ID from a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item_id: str
            The ID of the item to retrieve

        Returns:
        - Category or None:
            The item if found, None otherwise

        """
        cdb = get_categories_db()
        for category in cdb["categories"]:
            if category["id"] == category_id:
                return category
            else:
                return None



    @staticmethod
    def insert_category(category: Category) -> Category:
        """
        Insert an item into a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item: Category
            The item to insert

        Returns:
        - Category:
            The inserted item

        """

        cdb = get_categories_db()
        cdb.append(category.model_dump())
        print(cdb)
        write_categories_db(cdb)
        return category

    @staticmethod
    def update_category(category_id: str, categoryupdt: Category):
        cdb = get_categories_db()
        for category in cdb["categories"]:
            if category["id"] == category_id:
                category["name"] = categoryupdt["name"]
                # segue nessa mesma logica para os outros campos

        write_categories_db(cdb)

    @staticmethod
    def delete_category(category_id: str) -> list:
        """
        Delete an item of a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item is stored
        - item_id: str
            The ID of the item to delete

        Returns:
        - list:
            A list of all itens in the collection.

        """
        cdb = get_categories_db()
        for category in cdb:
            if category["id"] == category_id:
                index = cdb.index(category)
                cdb.pop(index)
        write_categories_db(cdb)
        return cdb


