import json

from ...schemas.response import HttpResponseModel, HTTPResponses

USER_DATABASE_FILE = "src/features/users/data/users.json"



def read_json() -> dict:
    with open(USER_DATABASE_FILE, 'r') as u:
        udb = json.load(u)
    return udb


def get_user_by_username(username: str) -> HttpResponseModel:
    data = read_json()
    users = data["users"]
    for user in users:
        if username == user["cpf"] or username == user["email"]:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_FOUND().message,
                status_code=HTTPResponses.CATEGORY_FOUND().status_code,
                data=user,
            )
        else:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_FOUND().message,
                status_code=HTTPResponses.CATEGORY_NOT_FOUND().status_code,
                data={},
            )




