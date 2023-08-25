from fastapi import APIRouter
from src.api import categories

categories_router = APIRouter()
categories_router.include_router(categories.router, prefix="/categories", tags=["categories"])
