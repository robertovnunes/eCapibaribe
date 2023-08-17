# pip3 install pytest httpx pytest_bdd
# python3 -m pytest -v backend/src/tests/api/test_create_user.py

from pytest_bdd import scenario
from fastapi.testclient import TestClient
from src.api.create_user import cadastro, ROOT
import random

client = TestClient(cadastro)
CPF_PARA_TESTES = 99999999999



def test_sucesso():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "sucesso",
            "CPF": int(random.randint(10000000000, 99999999990)),
            "email": "teste_@email.com",
            "senha": "0laMundo!",
            "telefone": None,
            "dataNascimento": None
            },
         "expected_result":{
             "status_code": 200,
             "response": {"msg":"Cadastro realizado com sucesso"}
         }
    }
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
    
def test_falta_campo_obrigatorio():
    test_cases = [
        {
            "data":{   
                "nome": None,
                "sobrenome": "falta_campo_obrigatorio",
                "CPF": int(CPF_PARA_TESTES),
                "email": "teste@email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": None,
                "CPF": int(CPF_PARA_TESTES),
                "email": "teste@email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "falha",
                "CPF": None,
                "email": "teste@email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "teste",
                "CPF": int(CPF_PARA_TESTES),
                "email": None,
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "teste",
                "CPF": int(CPF_PARA_TESTES),
                "email": "teste@email.com",
                "senha": None,
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"Todos os campos obrigatórios devem ser preenchidos"}
            }
        }
    ] 
    
    for test in test_cases:
        response = client.post(ROOT, data=test["data"])
        assert response.status_code == test["expected_result"]["status_code"]
        assert response.json() == test["expected_result"]["response"]
    
    
def test_cpf_ja_cadastrado():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "cpf_existe",
            "CPF": int(12345678910),
            "email": "teste@email.com",
            "senha": "0laMundo!",
            "telefone": None,
            "dataNascimento": None
        },
        "expected_result":{
            "status_code": 200,
            "response": {"msg":"CPF já cadastrado"}
        }
    } 
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
    
def test_cpf_invalido():
    test_cases = [
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "cpf_invalido",
                "CPF": int(123456789101),
                "email": "teste@email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"CPF inválido"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "cpf_invalido",
                "CPF": int(1234567891),
                "email": "teste@email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"CPF inválido"}
            }
        },
    ] 
    
    for test in test_cases:
        response = client.post(ROOT, data=test["data"])
        assert response.status_code == test["expected_result"]["status_code"]
        assert response.json() == test["expected_result"]["response"]

def test_senha_sem_caractere_especial():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "senha_sem_caractere_especial",
            "CPF": int(CPF_PARA_TESTES),
            "email": "teste@email.com",
            "senha": "0laMundo",
            "telefone": None,
            "dataNascimento": None
        },
        "expected_result":{
            "status_code": 200,
            "response": {"msg":"Senha inválida! Falta caractere especial!"}
        }
    } 
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
def test_senha_sem_numero():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "senha_sem_numero",
            "CPF": int(CPF_PARA_TESTES),
            "email": "teste@email.com",
            "senha": "olaMundo!",
            "telefone": None,
            "dataNascimento": None
        },
        "expected_result":{
            "status_code": 200,
            "response": {"msg":"Senha inválida! Falta um número!"}
        }
    } 
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
    
def test_senha_sem_maiuscula():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "senha_sem_maiuscula",
            "CPF": int(CPF_PARA_TESTES),
            "email": "teste@email.com",
            "senha": "0lamundo!",
            "telefone": None,
            "dataNascimento": None
        },
        "expected_result":{
            "status_code": 200,
            "response": {"msg":"Senha inválida! Falta uma letra maiúscula!"}
        }
    } 
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
def test_email_ja_utilizado():
    test = {
        "data":{   
            "nome": "teste",
            "sobrenome": "email_ja_utilizado",
            "CPF": int(CPF_PARA_TESTES),
            "email": "teste@email.com",
            "senha": "0laMundo!",
            "telefone": None,
            "dataNascimento": None
        },
        "expected_result":{
            "status_code": 200,
            "response": {"msg":"E-mail já cadastrado"}
        }
    } 
    response = client.post(ROOT, data=test["data"])
    assert response.status_code == test["expected_result"]["status_code"]
    assert response.json() == test["expected_result"]["response"]
    
def test_email_inválido():
    test_cases = [
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "email_inválido",
                "CPF": int(CPF_PARA_TESTES),
                "email": "teste_email.com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"E-mail inválido"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "email_inválido",
                "CPF": int(CPF_PARA_TESTES),
                "email": "teste@email_com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"E-mail inválido"}
            }
        },
        {
            "data":{   
                "nome": "teste",
                "sobrenome": "email_inválido",
                "CPF": int(CPF_PARA_TESTES),
                "email": "testeemail_com",
                "senha": "0laMundo!",
                "telefone": None,
                "dataNascimento": None
            },
            "expected_result":{
                "status_code": 200,
                "response": {"msg":"E-mail inválido"}
            }
        }
    ] 
    for test in test_cases:
        response = client.post(ROOT, data=test["data"])
        assert response.status_code == test["expected_result"]["status_code"]
        assert response.json() == test["expected_result"]["response"]