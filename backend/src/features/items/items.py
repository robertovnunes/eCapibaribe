from fastapi import APIRouter
from .models.item_model import Item
from .list_items import get_single_item_with_cpf, get_with_cpf
from .create_items import create_new_item
from .modify_item import modify_item
from .delete_item import deletar_item

items_router = APIRouter()

@items_router.post("/api/items")
async def create_item(item: Item, file_name: str | None = None):
    msg:str = create_new_item(item, file_name)
    print(msg)
    return {"msg":msg}

@items_router.put("/api/items/update")
async def update_item(item: Item, file_name:str | None=None):
    msg:str = modify_item(item,file_name)
    return msg

@items_router.delete("/api/items/delete")
async def delete_item(id: int,cpf: str, file_name: str | None=None):
    id:int = deletar_item(id,cpf,file_name)
    return {"msg":id}

@items_router.get("/api/items/single")
async def get_single_item(id: int,cpf:str ,file_name:str | None=None):
    item: Item = get_single_item_with_cpf(id,cpf,file_name)
    return item

@items_router.get("/api/items/{cpf}")
async def list_items(cpf:str, file_name:str | None = None):
    items = get_with_cpf(cpf, file_name)
    return items