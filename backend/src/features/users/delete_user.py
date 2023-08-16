import json

from fastapi import HTTPException

def read_json(path: str) -> dict[list[dict]]:
    with open(path, 'r', encoding='utf-8') as json_file:
        employees_list = json.load(json_file)
    
    return employees_list  

def save_json(path: str, object: dict):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(object, json_file)

def delete_user_by_cpf(user_cpf: str, file_name: str) -> str:
    if file_name == None:
        file_name = "users"
    
    path = f"./features/users/data/{file_name}.json"
    data = read_json(path)
    users: list[dict] = data["users"]
    for idx, user in enumerate(users):
        if user_cpf == user["cpf"]:
            users.pop(idx)
            save_json(path, data)            
            return "Usuário deletado com sucesso"
    
    raise HTTPException(status_code=404, detail="Usuário não existe")