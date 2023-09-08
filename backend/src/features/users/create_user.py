# pip3 install fastapi uvicorn
# python3 -m uvicorn backend.src.features.users.create_user:cadastro --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/users/register
# http://localhost:8000/users/delete/711.880.474-69

import re
from fastapi import Request
from fastapi.templating import Jinja2Templates
import json
import os

print(os.getcwd())

CPF_PARA_TESTES = 99999999999
HOME_PATH = os.getcwd()
DATASET_PATH = HOME_PATH  + f"{os.sep}backend{os.sep}src{os.sep}db{os.sep}database{os.sep}usersdb.json"
TEMPLATES_PATH = HOME_PATH + f"{os.sep}backend{os.sep}src{os.sep}templates"
TEMPLATE_NAME = "create_user.html"

REQUEST_FIELDS = ["nome", "sobrenome", "cpf", "email", "senha", "telefone", "dataNascimento"]
MANDATORY_FIELDS = ["nome", "sobrenome", "cpf", "email", "senha"]

templates = Jinja2Templates(directory=TEMPLATES_PATH)

def transform_cpf(cpf: str) -> str:
    """Transforms CPF to number for validation

    Args:
        cpf (str): CPF gattered from request

    Returns:
        str: CPF without . or -
    """
    return cpf.replace(".", "").replace("-", "")

def validate_cpf(cpf: str) -> bool:
    """Checks if cpf is valid

    Args:
        cpf (str): CPF gattered from request

    Returns:
        bool: whether CPF is valid
    """
    try: 
        if len(transform_cpf(cpf)) == 11 and int(transform_cpf(cpf))>0:
            return True
        return False
    except:
        return False

class Cadastro():
    def __init__(self, request: Request) -> None:
        self.request = request
        self.request_dict = {}
        for key in REQUEST_FIELDS:
            self.request_dict[key] = None
        pass
    
    def __str__(self) -> str:
        string = ""
        for key in REQUEST_FIELDS:
            string += f"{key}: {self.request_dict[key]}\n"
        return string

    async def load_data(self) -> None:
        """loads request into Cadastro object
        """
        form = await self.request.form()
        for key in REQUEST_FIELDS:
            self.request_dict[key] = form.get(key)
        

    async def is_valid(self) -> (dict, dict):
        """Checks if request is valid and the user can be created

        Returns:
            tuple of dicts: dicts for data and response
        """
        with open(DATASET_PATH) as f:
            df = json.load(f)
            
        data = {key: [i[key] for i in df["users"]] for key in REQUEST_FIELDS}
        
        if any([key for key in MANDATORY_FIELDS if not self.request_dict[key]]):
            return None, {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
        
        for key in ["cpf", "email"]:
            if self.request_dict[key] in data[key]:
                return None, {"msg": f"{key} já cadastrado"}
        
        if not validate_cpf(self.request_dict["cpf"]):
            return None, {"msg":"CPF inválido"}
        
        if not re.search(r'[^a-zA-Z0-9\s]', self.request_dict["senha"]):
            return None, {"msg":"Senha inválida! Falta caractere especial!"}
        
        if not re.search(r'\d', self.request_dict["senha"]):
            return None, {"msg":"Senha inválida! Falta um número!"}
        
        if not re.search(r'[A-Z]', self.request_dict["senha"]):
            return None, {"msg":"Senha inválida! Falta uma letra maiúscula!"}
        
        if not re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.request_dict["email"]):
            return None, {"msg":"E-mail inválido"}
        
        return df, {"msg":"Cadastro realizado com sucesso"}
    

    
def get_templated_response(request: Request):
    return templates.TemplateResponse(TEMPLATE_NAME, {"request": request})

def save_user_in_db(data:dict, user:Cadastro):
    """Save user to database

    Args:
        data (dict): data from database
        user (Cadastro): data from request
    """
    if data is not None:
        dic = {}
        for key in REQUEST_FIELDS:
            dic[key] = user.request_dict[key]
        
        data["users"].append(dic)
        if int(transform_cpf(dic["cpf"])) != CPF_PARA_TESTES:
            with open(DATASET_PATH, "w") as f:
                f.write(json.dumps(data, indent=4))