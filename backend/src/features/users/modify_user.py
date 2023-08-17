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

def modify_user(new_user_data: User, file_name: str | None) -> User:
    if file_name == None:
        file_name = "users"
        
    path = f"./features/users/data/{file_name}.json"
    data = read_json(path)
    user_cpf = new_user_data.cpf
    users: list[dict] = data["users"]
    for idx, user in enumerate(users):
        if user_cpf == user["cpf"]:
            print("aaaaa")
            data["users"][idx] = vars(new_user_data)
            print("xxxxx")
            save_json(path, data)            
            return "Usuário modificado com sucesso"
    
    raise HTTPException(status_code=404, detail="User not found")