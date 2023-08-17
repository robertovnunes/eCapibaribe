from .schemas.response import HTTPResponses, HttpResponseModel
from .pytest_bdd import parsers, given, when, then, scenario, scenarios
from .service.impl.category_service import categoryService
from .tests.api.utils.utils import get_response_categories_list, req_type_to_function


@scenario('../features/category-itens.feature', 'Obter categoria por ID')
def test_get_category_by_id():
    pass


@scenario('../features/category-itens.feature', 'Obter todas as categorias')
def test_get_all_categories():
    pass


@given(parsers.cfparse('a categoria "{category_name}" existe no banco de dados'))
def mock_category_service_response(category_name: str):
    pass


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


@then(parsers.cfparse('o corpo da resposta deve conter o id da categoria igual a "{category_id}"'))
def check_response_body_id(context, category_id: str):
    """
    Check if the response body is a json with the given category id

    Args:
        context: pytest-bdd context
        category_id (str): category id

    """

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
@then("a categoria com id igual a <id> e nome igual a <nome>")
def check_all_response_body_id(context, id, nome):
    """
    Check if each category in the response body has an id

    Args:
        nome (str):
        id (str):
        context: pytest-bdd context

    """
    response = get_response_categories_list
    response_body = response.json()["data"]["categories"]
    response_body = context["response"].json()["data"]["categories"]
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
