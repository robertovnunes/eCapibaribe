from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.category_service import categoryService
from src.tests.api.utils.utils import get_response_categorys_list, req_type_to_function

""" Scenario: Obter category por ID """


# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Obter categoria por ID", feature_name="../features/category-itens.feature")
def test_get_category():
    """ Get category by id """


"""
Note:
    In the following step definitions, the parsers.cfparse() method is used to parse 
    the step definition strings. It is important to know that without this parse, 
    the step definitions will not be recognized by pytest-bdd.
"""


# Step definitions for the "Obter category por ID" scenario
@given(parsers.cfparse('o categoryService retorna uma categoria com id "{category_id}"'))
def mock_category_service_response(category_id: str):
    """
    Mock the categoryService.get_category() method to return an category with the given id and name
    """

    categoryService.get_category = lambda id: HttpResponseModel(
        message=HTTPResponses.category_FOUND().message,
        status_code=HTTPResponses.category_FOUND().status_code,
        data={"id": category_id}
    )


@when(parsers.cfparse('uma requisição "{req_type}" for enviada para "{req_url}"'), target_fixture="context")
def send_get_category_request(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context


@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].status_code == int(status_code)
    return context


@then(parsers.cfparse('o JSON da resposta deve conter id "{category_id}" e nome "{category_name}"'),
      target_fixture="context")
def check_response_json_contains_category_data(context, category_id: str, category_name: str):
    """
    Check if the response JSON contains the category id and name
    """

    expected_data = {
        "id": category_id,
        "name": category_name
    }
    assert context["response"].json()["data"] == expected_data
    return context


""" Scenario: Obter todos os itens """


@scenario(scenario_name="Obter todos os itens", feature_name="../features/category-itens.feature")
def test_get_categorys():
    """ Get all categorys """


# Step definitions for the "Obter todos os itens" scenario
@given(parsers.cfparse('o categoryService retorna uma lista de categorias'))
def mock_category_service_response_list():
    """
    Mock the categoryService.get_categorys() method to return a list of categorys
    """
    categoryService.get_categorys = lambda: HttpResponseModel(
        message=HTTPResponses.category_FOUND().message,
        status_code=HTTPResponses.category_FOUND().status_code,
        data={
            'categorys': [
                {"id": "123", "name": "Bebidas"},
                {"id": "456", "name": "Brinquedos"}
            ]
        }
    )


@then(parsers.cfparse('a categoria com id "{category_id}" e nome "{category_name}" está na lista'),
      target_fixture="context")
@given(parsers.cfparse('a categoria com id "{category_id}" e nome "{category_name}" está na lista'),
       target_fixture="context")
def check_category_is_in_list(context, category_id: str, category_name: str):
    """
    Check if the category with the given id and name is in the response list
    """
    categorys = get_response_categorys_list(context["response"])

    assert {"id": category_id, "name": category_name} in categorys

    return context


@then(parsers.cfparse('o JSON da resposta deve ser uma lista de itens'), target_fixture="context")
def check_response_json_is_an_category_list(context):
    """
    Check if the response JSON is a list of categorys
    """

    categorys = get_response_categorys_list(context["response"])

    assert isinstance(categorys, list)
    for category in categorys:
        assert isinstance(category, dict)
        assert "name" in category and isinstance(category["name"], str)
        assert "id" in category and isinstance(category["id"], str)

    return context


@given('o categoryService não retorna um category com id "123"')
def step_impl():
    raise NotImplementedError(u'STEP: Given o categoryService não retorna um category com id "123"')


@given('o categoryService não retorna um categoria com id "123"')
def step_impl():
    raise NotImplementedError(u'STEP: Given o categoryService não retorna um categoria com id "123"')


@given("o categoryService retorna uma lista de itens")
def step_impl():
    raise NotImplementedError(u'STEP: Given o categoryService retorna uma lista de itens')


@given('eu recebo um JSON contendo o token "token"')
def step_impl():
    raise NotImplementedError(u'STEP: And eu recebo um JSON contendo o token "token"')


@given('id "id", nome "nome", email "email" e tipo de usuario "administrador"')
def step_impl():
    raise NotImplementedError(u'STEP: And id "id", nome "nome", email "email" e tipo de usuario "administrador"')


@given("a categoria não existe no banco de dados")
def step_impl():
    raise NotImplementedError(u'STEP: And a categoria não existe no banco de dados')


@given('não existe a categoria "bebidas" no banco de dados')
def step_impl():
    raise NotImplementedError(u'STEP: Given não existe a categoria "bebidas" no banco de dados')


@when('uma requisição "POST" for enviada para "/categorias" com o JSON:')
def step_impl():
    raise NotImplementedError(u'STEP: When uma requisição "POST" for enviada para "/categorias" com o JSON:
                              """
                              {
                                "nome": "Bebidas",
                                "descricao": "Bebidas em geral",
                                "imagem": "http://picsum.photos/200/300",
                                "keywords": ["bebidas", "refrigerantes", "cervejas"]
                              }
                              """')
                              )
