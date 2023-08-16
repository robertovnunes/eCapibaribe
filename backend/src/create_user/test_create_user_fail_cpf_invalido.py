# pip3 install pytest httpx pytest_bdd
# python3 -m pytest -v backend/src/create_user/

from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient
from backend.src.create_user.create_user import cadastro, ROOT
import random

client = TestClient(cadastro)
CPF_PARA_TESTES = 99999999999


@scenario("test_cadastro.feature", "Cadastro com CPF inválido")
def test_bdd_cpf_inválido(context):
    """ Get all items """
    return ""

@given(parsers.parse('o usuário de CPF "1234567891" não está cadastrado no sistema'))
def usuario_nao_cadastrado_por_cpf():
    # Simular verificação de usuário não cadastrado por CPF
    pass

@when(parsers.parse('o sistema recebe o pedido para criar o usuário'))
def cria_user():
    # Simular verificação de usuário não cadastrado por CPF
    pass

@when(parsers.parse('com o nome com "{nome}"'))
def com_nome(context, nome):
    context["nome"] = nome

@when(parsers.parse('com o e-mail com "{email}"'))
def com_email(context,email):
    context["email"] = email

@when(parsers.parse('com o CPF com "{cpf}"'))
def com_cpf(context,cpf):
    context["cpf"] = cpf

@when(parsers.parse('com o sobrenome com "{sobrenome}"'))
def com_sobrenome(context,sobrenome):
    context["sobrenome"] = sobrenome

@when(parsers.parse('com a senha com "{senha}"'))
def com_senha(context,senha):
    context["senha"] = senha
    
@then(parsers.parse('o sistema cadastra o usuário'))
def cadastro():
    # Simular verificação de usuário não cadastrado por CPF
    pass

@then(parsers.parse('o sistema envia erro "{mensagem}"'))
def envia_mensagem_de_sucesso(context, mensagem):
    print(context)
    response = client.post(ROOT, data={
        "nome": context["nome"],
        "sobrenome": context["sobrenome"],
        "CPF": context["cpf"],
        "email": context["email"],
        "senha": context["senha"],
        "telefone": None,
        "dataNascimento": None
    })
    assert response.status_code == 200
    assert response.json() == {"msg":mensagem}
    pass

