import json as json
from uuid import uuid4
from logging import INFO, WARNING, getLogger

CATEGORY_DATABASE_FILE = "src/db/database/categorydb.json"
ITEM_DATABASE_FILE = "src/db/database/itensdb.json"
USER_DATABASE_FILE = "src/db/database/usersdb.json"

logger = getLogger('uvicorn')


def get_categories_db():
    with open(CATEGORY_DATABASE_FILE) as c:
        cdb = json.load(c)
    return cdb


def get_itens_db():
    with open(ITEM_DATABASE_FILE) as i:
        idb = json.load(i)
    return idb


def get_users_db():
    with open(USER_DATABASE_FILE) as u:
        udb = json.load(u)
    return udb


def write_categories_db(cdb):
    with open(CATEGORY_DATABASE_FILE, 'w') as c:
        json.dump(cdb, c)


def write_itens_db(idb):
    with open(ITEM_DATABASE_FILE, 'w') as i:
        json.dump(idb, i)


class database:

    def get_all_itens(self) -> list:

        """
        Get all itens from a collection

        Parameters:
        - collection_name: str
            The name of the collection

        Returns:
        - list
            A list of all itens in the collection

        """
        idb = get_itens_db()
        return idb

    def get_item_by_id(self, item_id: str) -> dict:
        """
        Retrieve an item by its ID from a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item_id: str
            The ID of the item to retrieve

        Returns:
        - dict or None:
            The item if found, None otherwise
        """
        idb = get_itens_db()
        for item in idb["itens"]:
            if item["id"] == item_id:
                return item

    def insert_item(self, item: dict) -> dict:
        """
        Insert an item into a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item: dict
            The item to insert

        Returns:
        - dict:
            The inserted item

        """
        # TODO: test if this method works
        idb = get_itens_db()
        item["id"] = str(uuid4())[:self.ID_LENGTH]
        item_id = idb.insert_one(item).inserted_id
        return {
            "id": str(item_id),
            **item
        }

        # TODO: implement update_item method
        # def update_item(self, collection_name: str, item_id: str, item: dict) -> dict:
        """
        Update an item in a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item is stored
        - item_id: str
            The ID of the item to update
        - item: dict
            New item data

        Returns:
        - dict:
            The updated item

        """

        # TODO: implement delete_item method
        # def delete_item(self, collection_name: str, item_id: str) -> list:
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

    def get_all_categories(self) -> list:
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

    def get_category_by_id(self, category_id: str) -> dict:
        """
        Retrieve an item by its ID from a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item_id: str
            The ID of the item to retrieve

        Returns:
        - dict or None:
            The item if found, None otherwise

        """
        cdb = get_categories_db()
        for category in cdb["categories"]:
            if category["id"] == category_id:
                return category

    def insert_category(self,category_id: str, category: dict) -> dict:
        """
        Insert an item into a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item: dict
            The item to insert

        Returns:
        - dict:
            The inserted item

        """

        cdb = get_categories_db()
        cdb["categories"].append(category)
        write_categories_db(cdb)




    def update_category(self, category_id: str, categoryupdt: dict) -> dict:
        cdb = get_categories_db()
        for category in cdb["categories"]:
            if category["id"] == category_id:
                category["name"] = categoryupdt["name"]
                #segue nessa mesma logica para os outros campos

        write_categories_db(cdb)





    def delete_category(self, category_id: str) -> list:
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
        for category in cdb["categories"]:
            if category["id"] == category_id:
                cdb["categories"].pop(category)

        write_categories_db(cdb)

    def get_all_users(self) -> list:
        """
        Get all users from a collection

        Parameters:
        - collection_name: str
            The name of the collection

        Returns:
        - list
            A list of all users in the collection

        """
        udb = get_users_db()
        return udb

    def get_user_by_id(self, user_id: str) -> dict:
        """
        Retrieve an item by its ID from a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item_id: str
            The ID of the item to retrieve

        Returns:
        - dict or None:
            The item if found, None otherwise

        """

        udb = get_users_db()
        for user in udb["users"]:
            if user["id"] == user_id:
                return user

    def insert_user(self, user: dict) -> dict:
        """
        Insert an item into a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item will be stored
        - item: dict
            The item to insert

        Returns:
        - dict:
            The inserted item

        """
        # TODO: test if this method works

        user["id"] = str(uuid4())[:self.ID_LENGTH]
        udb = get_users_db()
        user_id = udb.insert_one(user).inserted_id
        return {
            "id": str(user_id),
            **user
        }

        # TODO: implement update_item method
        # def update_item(self, collection_name: str, item_id: str, item: dict) -> dict:
        """
        Update an item in a collection

        Parameters:
        - collection_name: str
            The name of the collection where the item is stored
        - item_id: str
            The ID of the item to update
        - item: dict
            New item data

        Returns:
        - dict:
            The updated item

        """

        # TODO: implement delete_item method
        # def delete_item(self, collection_name: str, item_id: str) -> list:
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


