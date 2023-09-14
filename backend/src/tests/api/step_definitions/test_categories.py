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
    response_body = context["response"].json()["data"]
    assert response_body["id"] == category_id


@then(parsers.cfparse('o corpo da resposta deve conter o nome da categoria igual a "{category_name}"'))
def check_response_body_name(context, category_name: str):
    """
    Check if the response body is a json with the given category name

    Args:
        context: pytest-bdd context
        category_name (str): category name

    """

    response_body = context["response"].json()["data"]
    assert response_body["name"] == category_name


@then(parsers.cfparse('o corpo da resposta deve conter a descrição da categoria igual a "{category_description}"'))
def check_response_body_description(context, category_description: str):
    """
    Check if the response body is a json with the given category description

    Args:
        context: pytest-bdd context
        category_description (str): category description

    """

    response_body = context["response"].json()["data"]
    assert response_body["description"] == category_description


@then(parsers.cfparse('o corpo da resposta deve conter a url da imagem da categoria igual a "{category_image_url}"'))
def check_response_body_image_url(context, category_image_url: str):
    """
    Check if the response body is a json with the given category image url

    Args:
        context: pytest-bdd context
        category_image_url (str): category image url

    """

    response_body = context["response"].json()["data"]
    assert response_body["image_url"] == category_image_url


@then(parsers.cfparse(
    'o corpo da resposta deve conter a lista de palavras-chave da categoria igual a "{category_keywords}"'))
def check_response_body_keywords(context, category_keywords: str):
    """
    Check if the response body is a json with the given category image url

    Args:
        context: pytest-bdd context
        category_keywords (str): category keywords

    """

    response_body = context["response"].json()["data"]
    assert response_body["keywords"] == category_keywords


@then(parsers.cfparse('o JSON da resposta deve ser uma lista com "{total}" categorias'), target_fixture="context")
def check_response_body_is_a_list(context, total):
    """
    Check if the response body is a list of categories

    Args:
        total:
        context: pytest-bdd context

    """
    response_body = context["response"].json()["data"]["categories"]
    assert len(response_body) == int(total)


@then(parsers.cfparse('a categoria com id igual a {id} e nome igual a {nome}'), target_fixture="context")
def check_all_response_body_id(context, id, nome):
    """
    Check if each category in the response body has an id

    Args:
        nome (str):
        id (str):
        context: pytest-bdd context

    """
    response = get_response_categories_list(context["response"])
    response_body = response.json()["data"]["categories"]
    for category in response_body:
        print(category["id"], type(category["name"]), type(nome))
        if category["id"] == id:
            assert category["name"] == nome


@then(parsers.cfparse("descrição igual a {desc}"))
def check_all_response_body_desc(context, desc):
    """
    Check if each category in the response body has an id

    Args:
        desc (str):
        context: pytest-bdd context

    """

    response_body = context["response"].json()["data"]["categories"]
    for category in response_body:
        assert category['description'] == desc


@then(parsers.cfparse('imagem igual a {image}'))
def check_all_response_body_image(context, image):
    """
    Check if each category in the response body has an id

    Args:
        image (str):
        context: pytest-bdd context

    """

    response_body = context["response"].json()["data"]["categories"]
    for category in response_body:
        assert category["image__url"] == image


@then(parsers.cfparse('palavras-chave igual a {keywords}'))
def check_all_response_body_keywords(context, keywords):
    """
    Check if each category in the response body has an id

    Args:
        keywords (str):
        context: pytest-bdd context

    """

    response_body = context["response"].json()["data"]
    for category in response_body:
        assert category["keywords"] == keywords


@then(parsers.cfparse('lista de itens igual a {itens}'))
def check_all_response_body_itens(context, itens):
    """
    Check if each category in the response body has an id

    Args:
        itens (str):
        context: pytest-bdd context

    """

    response_body = context["response"].json()["data"]
    for category in response_body:
        assert category['itens'] == itens


@when('uma requisição "POST" for enviada para "/categories" com o JSON')
def send_post_category_request(client, context):
    """
    Send a request to the given URL using the given request type
    """

    response = req_type_to_function(client, "POST")("/categories", json=context.text)
    context["response"] = response
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
