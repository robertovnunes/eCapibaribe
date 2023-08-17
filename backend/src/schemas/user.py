from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class UserModel(BaseModel):
    name: str
    email: str
    password: str
    cpf: str


class UserGet(BaseModel):
    id: str
    name: str
    email: str
    password: str
    cpf: str


class UserList(BaseModel):
    users: list[UserGet]
