from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario, scenarios
from src.service.impl.category_service import categoryService
from src.tests.api.utils.utils import get_response_categories_list, req_type_to_function

db_file_name = "categorie_test.json"

@scenario('../features/buscar_categorias.feature', 'Obter categoria por nome')
def test_get_category_by_name():
    pass

@given(parsers.cfparse('a categoria "{category_name}" existe no banco de dados'))
def mock_category_service_response(category_name: str):
    pass


@when(parsers.cfparse('uma requisição GET for enviada para "{req_url}"'), target_fixture="context")
def send_get_category_request(client, context, req_url: str):
    response = req_type_to_function(client, "GET")(req_url)
    context["response"] = response
    return context


@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context


@then(parsers.cfparse('o corpo da resposta deve conter o id da categoria igual a "{category_id}"'))
def check_response_body_id(context, category_id: str):
    response_body = context["response"].json()["data"]
    assert response_body["id"] == category_id


@then(parsers.cfparse('o corpo da resposta deve conter o nome da categoria igual a "{category_name}"'))
def check_response_body_name(context, category_name: str):
    response_body = context["response"].json()["data"]
    assert response_body["name"] == category_name


@then(parsers.cfparse('o corpo da resposta deve conter a descrição da categoria igual a "{category_description}"'))
def check_response_body_description(context, category_description: str):
    response_body = context["response"].json()["data"]
    assert response_body["description"] == category_description


@then(parsers.cfparse('o corpo da resposta deve conter a url da imagem da categoria igual a "{category_image_url}"'))
def check_response_body_image_url(context, category_image_url: str):
    response_body = context["response"].json()["data"]
    assert response_body["image_url"] == category_image_url


@then(parsers.cfparse(
    'o corpo da resposta deve conter a lista de palavras-chave da categoria igual a "{category_keywords}"'))
def check_response_body_keywords(context, category_keywords: str):
    response_body = context["response"].json()["data"]
    assert response_body["keywords"] == category_keywords


##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
