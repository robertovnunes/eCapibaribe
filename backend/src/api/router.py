from fastapi import APIRouter

from . import categories
from features.users import user

api_router = APIRouter()
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(user.users_router, prefix="/users", tags=["users"])