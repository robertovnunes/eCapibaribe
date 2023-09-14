from fastapi import APIRouter, Request
from .models.user_model import User
from .modify_user import modify_user
from .delete_user import delete_user_by_cpf
from .get_user import get_user_by_username
from .create_user import Cadastro, save_user_in_db


users_router = APIRouter()

@users_router.get("/username")
async def get_user(username: str):
    user = get_user_by_username(username)
    return {
        "data": user
    }


@users_router.put("/users/modify")
async def modify_user(user: User, file_name: str | None = None):
    success_message = modify_user(user, file_name)
    return {
        "message": success_message
    }


@users_router.delete("/users/delete/{cpf}")
async def delete_user(cpf: str, file_name: str | None = None):
    success_message = delete_user_by_cpf(cpf, file_name)
    return {
        "message": success_message
    }


@users_router.post("/api/users/register")
async def register_user(request: Request):
    print(await request.json())
    user = Cadastro(request)
    await user.load_data()
    data, response = await user.is_valid()
    save_user_in_db(data, user)
    return response