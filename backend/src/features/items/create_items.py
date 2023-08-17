import json
from fastapi import HTTPException
from .models.item_model import Item


def read_json(path: str) -> dict[list[dict]]: 
    with open(path, 'r', encoding='utf-8') as json_file:       
        employees_list = json.load(json_file)       
    return employees_list

def save_json(path: str, object: dict):
    with open(path, 'w', encoding='utf-8') as json_file:       
        json.dump(object, json_file)

def create_new_item(new_item: Item, file_name: str | None) -> str:
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    for item in items:
        #if cpf == item["cpf_user"] and new_item.item_id == item["item_id"]:
        if new_item.item_id == item["item_id"]:
            raise HTTPException(status_code=409, detail="Id already exist")
    data["items"].append(vars(new_item))
    save_json(path, data)
    return "Item registrado com sucesso!"