from fastapi import APIRouter
from .models.user_model import User
from .delete_user import delete_user_by_cpf


users_router = APIRouter()

@users_router.post("/users/modify")
async def create_item(item: User):
    return item

@users_router.delete("/users/delete/{cpf}")
async def delete_user(cpf: str):
    success_message = delete_user_by_cpf(cpf)
    return {
        "message": success_message
    }
