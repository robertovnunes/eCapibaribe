import pytest
from pytest_bdd import parsers, given, when, then, scenario
from fastapi.testclient import TestClient

db_file_name = "users_test"

""" Scenario: Modificar dados do usuário com sucesso """
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Modificar dados do usuário com sucesso", feature_name="../features/cadastro_de_usuarios.feature")
def test_modify_user():
    """modify user"""

@given(parsers.cfparse("o usuário de CPF {cpf} existe no sistema"))
def mock_user_in_system(cpf: str):
    return {
        "cpf": cpf
    }

@when(
    parsers.cfparse('uma requisição DELETE for enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_delete_user_request(client: TestClient, context, req_url: str):
    """
    Send a request to the given URL using the given request type
    """
    response = client.delete(req_url, params={"file_name": db_file_name})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve conter o campo "{key}" com o valor "{value}"'), target_fixture="context")
def check_response_status_code(context, key: str, value: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].json() == {key: value}
    return context


""" Scenario: Falha ao deletar usuário - usuário não existe """
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Falha ao deletar usuário - usuário não existe", feature_name="../features/cadastro_de_usuarios.feature")
def test_delete_user_not_found():
    """delete user not found"""

@given(parsers.cfparse("o usuário de CPF {cpf} não existe no sistema"))
def mock_user_not_found_in_system(cpf: str):
    return {
        "cpf": cpf
    }

@when(
    parsers.cfparse('uma requisição DELETE for enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_get_item_request(client: TestClient, context, req_url: str):
    """
    Send a request to the given URL using the given request type
    """
    response = client.delete(req_url, params={"file_name": db_file_name})
    context["response"] = response
    return context





""" Scenario: Deletar o usuário com sucesso """
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Deletar o usuário com sucesso", feature_name="../features/cadastro_de_usuarios.feature")
def test_delete_user():
    """delete user"""



#@then(
#    parsers.cfparse('o JSON da resposta deve conter id "{item_id}" e nome "{item_name}"'), 
#    target_fixture="context"
#)
#def check_response_json_contains_item_data(context, item_id: str, item_name: str):
#    """
#    Check if the response JSON contains the item id and name
#    """
#
#    expected_data = { "id": item_id, "name": item_name }
#    assert context["response"].json()["data"] == expected_data
#    return context
