from fastapi import APIRouter

from . import categories

categories_router = APIRouter()
categories_router.include_router(categories.router, prefix="/categories", tags=["categories"])
