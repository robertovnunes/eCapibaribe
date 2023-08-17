import pytest
from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient

db_file_name = "item_test.json"

""" Scenario: Registrar item com sucesso """
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Registrar item com sucesso", feature_name="../features/registro_de_items.feature")
def test_register_item():
    """Register item"""
    pass

@given(parsers.cfparse('o item de id  "{item_id}" não está registrado'))
def item_nao_registrado():
    pass

@when(parsers.cfparse('o usuario de cpf "{user_cpf}" registra o item'), target_fixture= "context")
def cpf_item_register(context, user_cpf):
    context["user_cpf"] = user_cpf
    return context

@when(parsers.cfparse('o sistema recebe a requisição POST para "{req_url}" para registrar o Item'), target_fixture="context")
def get_route(context, req_url):
    context["req_url"] = req_url
    print(context)
    return context

@when(parsers.cfparse('com o id "{item_id}"'), target_fixture= "context")
def insert_item_id(context, item_id):
    context["item_id"] = item_id
    return context

@when(parsers.cfparse("{field}" "{value}"), target_fixture = "context")
def insert_item_values(context, field, value):
    context[field] = value
    return context 

@then(parsers.cfparse('o sistema registra o item'), target_fixture="context")
def resgistrar(context):
  return context

@then(parsers.cfparse('o sistema envia uam mensagem "{mensagem}"'), target_fixture="context")
def post_request(client: TestClient, context, mensagem):
   response = client.post(context["req_url"], data={
        "cpf_user": context["cpf_user"],
        "item_id": context["item_id"],
        "item_nome": context["nome"],
        "item_price": context["preço"],
        "quantidade":context["quantidade"],
        "marca": context["marca"],
        "categoria": context["marca"],
        "descricao": context["descricao"],
        "imagem": context["imagem"],
        "op_envio": context["op_envio"],
        "palavrachave": context["palavrachave"]
   }, params={"file_name": db_file_name})
   assert response.status_code == 200
   assert response.json() == {"msg":mensagem}