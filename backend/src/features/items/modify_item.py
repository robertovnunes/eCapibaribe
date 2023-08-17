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


def modify_item(new_item:Item,file_name: str |None ) -> str:    
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    for idX, item in enumerate(items):
        if new_item.item_id == item["item_id"]:
            data["items"][idX]=vars(new_item)
    save_json(path, data)
    return "Informações do item id {} alteradas com sucesso!".format(str(new_item.item_id))