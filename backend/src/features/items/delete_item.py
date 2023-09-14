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

def deletar_item(id:int,cpf: str, file_name: str |None ) -> str:    
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    for idX, item in enumerate(items):
        if id == item["item_id"] and cpf == item["cpf_user"]:
            data["items"].pop(idX)
            save_json(path, data)
            return id
    raise HTTPException(status_code=409, detail="Id already exist")


    
    
