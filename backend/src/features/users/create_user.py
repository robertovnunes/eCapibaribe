# pip3 install fastapi uvicorn
# python3 -m uvicorn backend.src.features.users.create_user:cadastro --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/users/register

import re
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
import json


CPF_PARA_TESTES = 99999999999

PATH = "./features/users"
DATASET_PATH = PATH + "/data/users.json"
TEMPLATES_PATH = PATH + "/templates"
ROOT = "/users/register"
cadastro = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory=TEMPLATES_PATH)

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

    async def load_data(self) -> None:
        form = await self.request.form()
        self.nome = form.get("nome")
        self.sobrenome = form.get("sobrenome")
        self.CPF = form.get("cpf")
        self.email = form.get("email")
        self.senha = form.get("senha")
        self.telefone = form.get("telefone")
        self.dataNascimento = form.get("dataNascimento")
        

    async def is_valid(self) -> (dict, str):
        with open(DATASET_PATH) as f:
            df = json.load(f)
        data = df["users"]
        
        data = {key: [i[key] for i in data] for key in data[0]}
        
        if self.CPF in ("", None) or self.nome in ("", None) or self.sobrenome in ("", None) or self.email in ("", None) or self.senha in ("", None):
            return None, {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
        
        elif int(self.CPF) in data["cpf"]:
            return None, {"msg":"CPF já cadastrado"}
        
        elif len(str(self.CPF)) != 11:
            return None, {"msg":"CPF inválido"}
        
        elif not re.search(r'[^a-zA-Z0-9\s]', self.senha):
            return None, {"msg":"Senha inválida! Falta caractere especial!"}
        
        elif not re.search(r'\d', self.senha):
            return None, {"msg":"Senha inválida! Falta um número!"}
        
        elif not re.search(r'[A-Z]', self.senha):
            return None, {"msg":"Senha inválida! Falta uma letra maiúscula!"}
        
        elif self.email in data["email"]:
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
    data, response = await user.is_valid()
    if data is not None:
        dic = { "nome": user.nome,
                "sobrenome": user.sobrenome,
                "cpf": int(user.CPF),
                "email": user.email,
                "senha": user.senha,
                "telefone": user.telefone,
                "dataNascimento": user.dataNascimento
                }
        print(dic)
        data["users"].append(dic)
        if int(user.CPF) != CPF_PARA_TESTES:
            with open(DATASET_PATH, "w") as f:
                f.write(json.dumps(data, indent=4))
    return response