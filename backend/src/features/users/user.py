from fastapi import APIRouter
from .models.user_model import User
from .modify_user import modify_user
from .delete_user import delete_user_by_cpf


users_router = APIRouter()

@users_router.post("/users/modify")
async def create_item(user: User, file_name: str | None = None):
    success_message = modify_user(user)
    return {
        "message": success_message
    }

@users_router.delete("/users/delete/{cpf}")
async def delete_user(cpf: str, file_name: str | None = None):
    success_message = delete_user_by_cpf(cpf, file_name)
    return {
        "message": success_message
    }
