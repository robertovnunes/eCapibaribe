from fastapi import APIRouter
from .models.item_model import Item
from .list_items import get_all_from_list
from .create_items import create_new_item

items_router = APIRouter()

@items_router.post("/items")
async def create_item(item: Item, file_name: str | None = None):
    msg:str = create_new_item(item, file_name)
    return msg

@items_router.get("/items/")
async def list_items(file_name:str | None = None):
    items = get_all_from_list()
    return items