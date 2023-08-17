from fastapi import APIRouter
from api import itens
from api import categories
from api import users

api_router = APIRouter()
api_router.include_router(itens.router, prefix="/itens", tags=["itens"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
