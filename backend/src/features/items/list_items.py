import json

def read_json(path: str) -> dict[list[dict]]: 
    with open(path, 'r', encoding='utf-8') as json_file:       
        employees_list = json.load(json_file)       
    return employees_list

def save_json(path: str, object: dict):
    with open(path, 'w', encoding='utf-8') as json_file:       
        json.dump(object, json_file)

def get_all_from_list(file_name: str | None):
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    return items

def get_with_cpf(cpf: str, file_name: str | None):
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    total_items: list[dict] = []
    for item in items:
        if cpf == item["cpf_user"]:
            total_items.append(item)
    return total_items

def get_single_item_with_cpf(id: int, cpf: str, file_name: str | None):
    if file_name == None:
        file_name = "item.json"
    path = f"./features/items/data/{file_name}"
    data = read_json(path)
    items: list[dict] = data["items"]
    for item in items:
        if cpf == item["cpf_user"] and id == item["item_id"]:
            return item