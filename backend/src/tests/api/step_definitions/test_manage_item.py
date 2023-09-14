import pytest
from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient

db_file_name = "item_test.json"
 
#Atualizar item
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Atualizar Item", feature_name="../features/atualizar_del_item.feature")
def test_update_item():
    pass

@given(parsers.cfparse('o item id "{item_id}" está registrado'))
def mock_user_in_system(item_id: int):
    return {
        "item_id": item_id
    }

@when(
    parsers.cfparse('uma requisição PUT for realizada na rota "{req_url}" com o corpo da requisição com o campo "{item_id}" juntamente com o "{item_price}"'), 
    target_fixture="context")
def send_put_item_request(client: TestClient, context, req_url: str, item_id:str, item_price:str):
    tempUpdateItem={"item_id":int(item_id),"item_price":float(item_price)}
    response = client.put(req_url, params={"file_name": db_file_name ,"item":tempUpdateItem})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve conter a mensagem "Informações do item id {item_id} alteradas com sucesso!"'), target_fixture="context")
def check_response_json(context, item_id: int):
    """parsers
    Check if the response status code is the expected
    """
    assert context["response"].json() == {"item_id": item_id}
    return context


@then(parsers.cfparse('o JSON da resposta deve conter o campo "{key}" do item id "{item_id}" com valor alterado'), target_fixture="context")
def check_response_json(context, key: str, item_id: str):
    """parsers
    Check if the response status code is the expected
    """
    assert context["response"].json() == {key: float(value)}
    return context








""" Remover Item """
@scenario(scenario_name="Remover Item", feature_name="../features/atualizar_del_item.feature")
def test_delete_item():
    """pass"""
    

@given(parsers.cfparse("o item id {id} está no registrado"))
def mock_user_not_found_in_system(id: int):
    return {
        "item_id": id
    }

@when(
    parsers.cfparse('uma requisição DELETE for realizada na rota "{req_url}" com o id do item "{id}" no corpo da requisição'), 
    target_fixture="context"
)
def send_delete_request(client: TestClient, context, req_url: str, id:str):
    path = f"{req_url}/{id}"
    response = client.delete(path, params={"file_name": db_file_name})
    context["response"] = response
    return context


@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """parsers
    Check if the response status code is the expected
    """
    assert context["response"].status_code == int(status_code)
    return context


@then(parsers.cfparse('o JSON da resposta deve conter o campo "{msg}" do item id "{value}"'), target_fixture="context")
def check_response_status_message(context, msg: str, value: str):
    """parsers
    Check if the response status code is the expected
    """
    assert context["response"].json() == {msg: int(value)}
    return context