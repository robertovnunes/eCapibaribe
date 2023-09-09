from pydantic import BaseModel
from datetime import datetime 

class User(BaseModel):
    nome: str
    sobrenome: str | None = None
    cpf: str
    email: str | None = None
    senha: str | None
    telefone: str | None
    dataNascimento: str | None