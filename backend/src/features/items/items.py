from fastapi import APIRouter
from .models.item_model import Item
from .list_items import get_all_from_list
from .create_items import create_new_item
from .modify_item import modify_item
from .delete_item import deletar_item
items_router = APIRouter()

@items_router.post("/items")
async def create_item(item: Item):
    msg:str = create_new_item(item)
    return msg

@items_router.get("/items/")
async def list_items():
    items = get_all_from_list()
    return items

@items_router.put("/items/update")
async def update_item(item: Item, file_name:str | None=None):
    msg:str = modify_item(item,file_name)
    return msg

@items_router.delete("/items/delete/{id}")
async def delete_item(id: int,file_name:str | None=None):
    id:int = deletar_item(id,file_name)
    return {"msg":id}