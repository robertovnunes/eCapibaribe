# pip3 install pytest httpx pytest_bdd
# python3 -m pytest -v tests/api/step_definitions/test_create_user.py

from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient
from features.users.create_user import CPF_PARA_TESTES
from features.users.user import users_router
import json

client = TestClient(users_router)

ROOT = "/api/users/register"

@scenario("../features/test_cadastro.feature", "Cadastro com sucesso")
def test_bdd_sucesso():
    """ Get all items """
    pass


@scenario("../features/test_cadastro.feature", "Faltam campos obrigatórios")
def test_bdd_falta_campo():
    """ Get all items """
    pass
      
@given(parsers.parse('usuário de email "teste_@email.com" não está cadastrado'), target_fixture="context")
def usuario_nao_cadastrado(context):
    # Simular verificação de usuário não cadastrado por email
    return context

@given(parsers.parse('usuário de cpf "99999999999" não está cadastrado'), target_fixture="context")
def usuario_nao_cadastrado_por_cpf(context):
    # Simular verificação de usuário não cadastrado por cpf
    return context

@when(parsers.parse('o sistema recebe o pedido para criar o usuário'), target_fixture="context")
def cria_user(context):
    # Simular verificação de usuário não cadastrado por cpf
    return context

@when(parsers.parse('com o nome com "{nome}"'), target_fixture="context")
def com_nome(context, nome):
    context["nome"] = nome
    return context
    
    
@when(parsers.parse('com o email com "{email}"'), target_fixture="context")
def com_email(context,email):
    context["email"] = email
    return context

@when(parsers.parse('com o cpf com "{cpf}"'), target_fixture="context")
def com_cpf(context,cpf):
    context["cpf"] = cpf
    return context

@when(parsers.parse('com o sobrenome com "{sobrenome}"'), target_fixture="context")
def com_sobrenome(context,sobrenome):
    context["sobrenome"] = sobrenome
    return context

@when(parsers.parse('com a senha com "{senha}"'), target_fixture="context")
def com_senha(context,senha):
    context["senha"] = senha
    return context
    
@then(parsers.parse('o sistema cadastra o usuário'), target_fixture="context")
def cadastro(context):
    # Simular verificação de usuário não cadastrado por cpf
    return context

@then(parsers.parse('envia mensagem de sucesso "{mensagem}"'), target_fixture="context")
def envia_mensagem(context, mensagem):
    print()
    response = client.post(ROOT, json={
        "nome": context["nome"],
        "sobrenome": context["sobrenome"],
        "cpf": context["cpf"],
        "email": context["email"],
        "senha": context["senha"],
        "telefone": None,
        "dataNascimento": None
    })
    assert response.status_code == 200
    assert response.json() == {"msg":mensagem}
    return context

      
@given(parsers.parse('usuário de email "teste@email.com" não está cadastrado'), target_fixture="context")
def usuario_nao_cadastrado(context):
    # Simular verificação de usuário não cadastrado por email
    return context



@scenario("../features/test_cadastro.feature", "Cadastro com cpf inválido")
def test_bdd_cpf_inválido(context):
    """ Get all items """
    pass

@given(parsers.parse('o usuário de cpf "1234567891" não está cadastrado no sistema'), target_fixture="context")
def usuario_nao_cadastrado_por_cpf(context):
    # Simular verificação de usuário não cadastrado por cpf
    return context




@scenario("../features/test_cadastro.feature", "Cadastro com email inválido")
def test_bdd_email_invalido(context):
    """ Get all items """
    pass
      
@given(parsers.parse('usuário de email "teste_@email.com" não está cadastrado no sistema'), target_fixture="context")
def usuario_nao_cadastrado(context):
    # Simular verificação de usuário não cadastrado por email
    return context

    

@scenario("../features/test_cadastro.feature", "Cadastro com email já utilizado")
def test_bdd_email_ja_existe(context):
    """ Get all items """
    pass
      
@given(parsers.parse('usuário de email "teste@email.com" está cadastrado no sistema'), target_fixture="context")
def usuario_nao_cadastrado(context):
    # Simular verificação de usuário não cadastrado por email
    return context


####


@scenario("../features/test_cadastro.feature", "Cadastro com senha inválida")
def test_bdd_fail_senha():
    """ Get all items """
    pass
      

    

@scenario("../features/test_cadastro.feature", "Cadastro com cpf já utilizado")
def test_bdd_cpf_existe():
    """ Get all items """
    pass

@given(parsers.parse('o usuário de cpf "12345678910" está cadastrado no sistema'), target_fixture="context")
def usuario_nao_cadastrado_por_cpf(context):
    # Simular verificação de usuário não cadastrado por cpf
    return context


@then(parsers.parse('o sistema envia erro "{mensagem}"'), target_fixture="context")
def envia_mensagem(context, mensagem):
    print(context)
    
    response = client.post(ROOT, json={
        "nome": context["nome"],
        "sobrenome": context["sobrenome"],
        "cpf": context["cpf"] if "cpf" in context.keys() else None,
        "email": context["email"],
        "senha": context["senha"],
        "telefone": None,
        "dataNascimento": None
    })
    assert response.status_code == 200
    assert response.json() == {"msg":mensagem}
    return context
