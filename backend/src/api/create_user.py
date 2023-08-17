# pip3 install fastapi uvicorn
# python3 -m uvicorn backend/src/api/create_user:cadastro --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/users/register

import re
import pandas as pd
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
import os

PATH = "src"
DATASET_PATH = PATH + "/data/users.csv"
ROOT = "/users/register"
cadastro = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="../templates")

class User():
    def __init__(self, request: Request) -> None:
        self.request = request
        self.nome = None
        self.sobrenome = None
        self.CPF = None
        self.email = None
        self.senha = None
        self.telefone = None
        self.dataNascimento = None
        pass

    async def load_data(self):
        form = await self.request.form()
        self.nome = form.get("nome")
        self.sobrenome = form.get("sobrenome")
        self.CPF = form.get("CPF")
        self.email = form.get("email")
        self.senha = form.get("senha")
        self.telefone = form.get("telefone")
        self.dataNascimento = form.get("dataNascimento")
        

    async def is_valid(self):
        df = pd.read_csv(DATASET_PATH, index_col="CPF")
        
        if self.CPF in ("", None) or self.nome in ("", None) or self.sobrenome in ("", None) or self.email in ("", None) or self.senha in ("", None):
            return None, {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
        
        elif int(self.CPF) in df.index:
            return None, {"msg":"CPF já cadastrado"}
        
        elif len(str(self.CPF)) != 11:
            return None, {"msg":"CPF inválido"}
        
        elif not re.search(r'[^a-zA-Z0-9\s]', self.senha):
            return None, {"msg":"Senha inválida! Falta caractere especial!"}
        
        elif not re.search(r'\d', self.senha):
            return None, {"msg":"Senha inválida! Falta um número!"}
        
        elif not re.search(r'[A-Z]', self.senha):
            return None, {"msg":"Senha inválida! Falta uma letra maiúscula!"}
        
        elif self.email in df["email"].values:
            return None, {"msg":"E-mail já cadastrado"}
        
        elif not re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email):
            return None, {"msg":"E-mail inválido"}
        
        return df, {"msg":"Cadastro realizado com sucesso"}
    

@cadastro.get(ROOT)
def get_user_info(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@cadastro.post(ROOT)
async def create_user(request: Request):
    user = User(request)
    await user.load_data()
    df, response = await user.is_valid()
    if df is not None:
        dic = { "nome": [user.nome],
                "sobrenome": [user.sobrenome],
                "CPF": [int(user.CPF)],
                "email": [user.email],
                "senha": [user.senha],
                "telefone": [user.telefone],
                "dataNascimento": [user.dataNascimento]
                }
        print(dic)
        df = pd.concat([df, pd.DataFrame.from_dict(dic).set_index("CPF", inplace=True)])
        df.to_csv(DATASET_PATH)
    return response