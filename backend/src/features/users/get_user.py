import json

from fastapi import HTTPException

USER_DATABASE_FILE = "./features/users/data/users.json"



def read_json() -> dict:
    with open(USER_DATABASE_FILE, 'r') as u:
        udb = json.load(u)
    return udb


def get_user_by_username(username: str) -> dict:
    data = read_json()
    users = data["users"]
    for user in users:
        if username == user["cpf"] or username == user["email"]:
            return user

    raise HTTPException(status_code=404, detail="Usuário não existe")



