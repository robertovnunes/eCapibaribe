from fastapi import APIRouter, Request
from .models.user_model import User
from .modify_user import modify_user_by_cpf
from .delete_user import delete_user_by_cpf
from .create_user import get_templated_response, Cadastro, create_user


users_router = APIRouter()

@users_router.put("/users/modify")
async def modify_user(user: User, file_name: str | None = None):
    success_message = modify_user_by_cpf(user, file_name)
    return {
        "message": success_message
    }

@users_router.delete("/users/delete/{cpf}")
async def delete_user(cpf: str, file_name: str | None = None):
    success_message = delete_user_by_cpf(cpf, file_name)
    return {
        "message": success_message
    }


@users_router.get("/users/register")
async def get_user_info(request: Request):
    return get_templated_response(request)


@users_router.post("/users/register")
async def register_user(request: Request):
    user = Cadastro(request)
    await user.load_data()
    data, response = await user.is_valid()
    return create_user(data, response, user)