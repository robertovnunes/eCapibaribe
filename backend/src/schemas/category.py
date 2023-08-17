from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class CategoryModel(BaseModel):
    name: str
    created_at: Optional[datetime]


class CategoryGet(BaseModel):
    id: str
    name: str
    created_at: Optional[datetime]


class CategoryList(BaseModel):
    categories: list[CategoryGet]
