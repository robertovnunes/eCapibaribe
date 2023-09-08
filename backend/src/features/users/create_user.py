# pip3 install fastapi uvicorn
# python3 -m uvicorn backend.src.features.users.create_user:cadastro --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/users/register


import re
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
import json
import os

print(os.getcwd())

CPF_PARA_TESTES = 99999999999
HOME_PATH = os.getcwd()
DATASET_PATH = HOME_PATH  + f"{os.sep}backend{os.sep}src{os.sep}db{os.sep}database{os.sep}usersdb.json"
TEMPLATES_PATH = HOME_PATH + f"{os.sep}backend{os.sep}src{os.sep}templates"

templates = Jinja2Templates(directory=TEMPLATES_PATH)

def transform_cpf(cpf: str) -> str:
    """Transforms CPF to number for validation

    Args:
        cpf (str): CPF gattered from form

    Returns:
        str: CPF without . or -
    """
    return cpf.replace(".", "").replace("-", "")

def validate_cpf(cpf: str) -> bool:
    try: 
        if len(transform_cpf(cpf)) == 11 and int(transform_cpf(cpf))>0:
            return True
        return False
    except:
        return False

class Cadastro():
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
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, sobrenome: {self.sobrenome}, CPF: {self.CPF}, email: {self.email}, senha: {self.senha}, telefone: {self.telefone}, data de nascimento: {self.dataNascimento}"

    async def load_data(self) -> None:
        form = await self.request.form()
        self.nome = form.get("nome")
        self.sobrenome = form.get("sobrenome")
        self.CPF = form.get("CPF")
        self.email = form.get("email")
        self.senha = form.get("senha")
        self.telefone = form.get("telefone")
        self.dataNascimento = form.get("dataNascimento")
        

    async def is_valid(self) -> (dict, dict):
        with open(DATASET_PATH) as f:
            df = json.load(f)
            
        data = {key: [i[key] for i in df["users"]] for key in df["users"][0]}
        
        if self.CPF in ("", None) or self.nome in ("", None) or self.sobrenome in ("", None) or self.email in ("", None) or self.senha in ("", None):
            return None, {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
        
        elif self.CPF in data["cpf"]:
            return None, {"msg":"CPF já cadastrado"}
        
        elif not validate_cpf(self.CPF):
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
    

    
def get_templated_response(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

def save_user_in_db(data:dict, user:Cadastro):
    if data is not None:
        dic = { "nome": user.nome,
                "sobrenome": user.sobrenome,
                "cpf": user.CPF,
                "email": user.email,
                "senha": user.senha,
                "telefone": user.telefone,
                "dataNascimento": user.dataNascimento
                }
        data["users"].append(dic)
        if int(transform_cpf(user.CPF)) != CPF_PARA_TESTES:
            with open(DATASET_PATH, "w") as f:
                f.write(json.dumps(data, indent=4))