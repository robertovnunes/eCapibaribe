import pytest
import json
from src.features.items.models.item_model import Item
from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient


db_file_name = "item_test.json"

""" Scenario: Registrar item com sucesso """
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Registrar item com sucesso", feature_name="../features/registro_de_items.feature")
def test_register_item():
    """Register item"""
    

@given(parsers.cfparse('o item de id  "{item_id}" não está registrado'))
def item_nao_registrado():
    return {}

@when(parsers.cfparse('o usuario de cpf "{cpf_user}" registra o item'), target_fixture="context")
def cpf_item_register(context, cpf_user):
    context["cpf_user"] = cpf_user
    return context

@when(parsers.cfparse('o sistema recebe a requisição POST para "{req_url}" para registrar o Item'), target_fixture="context")
def get_route(context, req_url):
    context["req_url"] = req_url
    return context

@when(parsers.cfparse('com o id "{item_id}"'), target_fixture= "context")
def insert_item_id(context, item_id):
    context["item_id"] = int(item_id)
    return context

@when(parsers.cfparse('"{field}" "{value}"'), target_fixture = "context")
def insert_item_values(context, field, value):
    if value.isnumeric():
        if value.isdigit():
            value = int(value)
        else: 
            value = float(value)
    
    context[field] = value
    return context 

@then(parsers.cfparse('o sistema registra o item'), target_fixture="context")
def resgistrar(context):
  return context

@then(parsers.cfparse('o sistema envia uma mensagem "{mensagem}"'), target_fixture="context")
def post_request(client: TestClient, context, mensagem):
   data = json.dumps({
        "cpf_user": context["cpf_user"],
        "item_id": context["item_id"],
        "item_nome": context["nome"],
        "item_price": context["preco"],
        "quantidade":context["quantidade"],
        "marca": context["marca"],
        "categoria": context["categoria"],
        "descricao": context["descricao"],
        "imagem": context["imagem"],
        "op_envio": context["op_envio"],
        "palavrachave": context["palavrachave"]
   })
   response = client.post("/items", content = data, params={"file_name": db_file_name})
   assert response.status_code == 200
   assert response.json() == {"msg":mensagem}

###################

@scenario(scenario_name="Falha ao registrar item com id repetido", feature_name="../features/registro_de_items.feature")
def test_register_item_2():
    """Register item"""
    

@given(parsers.cfparse('o item de id  "{item_id}" está registrado'))
def item_registrado():
    return {}


@then(parsers.cfparse('o sistema envia uma mensagem de erro "{mensagem}"'), target_fixture="context")
def post_request_2(client: TestClient, context, mensagem):
   data = json.dumps({
        "cpf_user": context["cpf_user"],
        "item_id": context["item_id"],
        "item_nome": context["nome"],
        "item_price": context["preco"],
        "quantidade":context["quantidade"],
        "marca": context["marca"],
        "categoria": context["categoria"],
        "descricao": context["descricao"],
        "imagem": context["imagem"],
        "op_envio": context["op_envio"],
        "palavrachave": context["palavrachave"]
   })
   response = client.post("/items", content = data, params={"file_name": db_file_name})
   assert response.status_code == 409
   assert response.json() == {"detail":mensagem}

############################
""" Mostrar itens registrados """
@scenario(scenario_name="Mostrar itens registrados", feature_name="../features/registro_de_items.feature")
def test_show_item():
    """Show item"""

@given(parsers.cfparse('que possuo items registrados'))
def item_registrado():
    """items registrados"""

@when(parsers.cfparse('uma requisição GET for enviada para "{req_url}"'), target_fixture="context")
def route_for_get(client:TestClient, context, req_url):
    response = client.get(req_url, params={"file_name": db_file_name})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o arquivo da resposta deve possuir uma lista com os items registrados'), target_fixture="context")
def get_items_registrados(context):
    assert type(context["response"].json()) == list