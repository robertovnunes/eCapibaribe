import json


from pytest_bdd import scenario, given, when, then, parsers

from src.tests.api.utils.utils import get_response_categories_list, req_type_to_function

url = "https://127.0.0.1/8000/categories"


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria')
def test_add_category():
    pass


@given(parsers.cfparse('a categoria "{name}" não existe no banco de dados'), target_fixture="context")
def check_category_not_exists(context, client, name):
    response = get_response_categories_list(req_type_to_function(client, "GET")(url))
    for category in response:
        assert category["name"] != name


@when(parsers.cfparse('uma requisição "POST" for enviada para "/categories" com o {Json}'), target_fixture="context")
def send_post_request(client, context, Json):
    context["Json"] = json.loads(Json)
    context["response"] = req_type_to_function(client, "POST")(url, json=context["Json"])

    return context


@given(parsers.cfparse('a categoria "{name}" existe no banco de dados'), target_fixture="context")
def check_category_exists(client, name):
    response = req_type_to_function(client, "GET")(url)
    categories = get_response_categories_list(response)
    for category in categories:
        assert category["name"] == name


@then(parsers.cfparse('a mensagem de erro deve ser "{message}"'), target_fixture="context")
def get_error_message(client, message):
    response = req_type_to_function(client, "POST")(url)
    assert response.json()["message"] == message
