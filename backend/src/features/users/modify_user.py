import json
from fastapi import HTTPException
from .models.user_model import User

def read_json(path: str) -> dict[list[dict]]:
    with open(path, 'r', encoding='utf-8') as json_file:
        employees_list = json.load(json_file)
    
    return employees_list  

def save_json(path: str, object: dict):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(object, json_file, default=str)

def modify_user(new_user_data: User) -> User:
    data = read_json("./features/users/data/users.json")
    user_cpf = new_user_data.cpf
    users: list[dict] = data["users"]
    for idx, user in enumerate(users):
        if user_cpf == user["cpf"]:
            data["users"][idx] = vars(new_user_data)
            save_json("./features/users/data/users.json", data)            
            return "Usuário modificado com sucesso"
    
    raise HTTPException(status_code=404, detail="User not found")