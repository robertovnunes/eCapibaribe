from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario, scenarios
from src.service.impl.category_service import categoryService
from src.tests.api.utils.utils import get_response_categories_list, req_type_to_function

db_file_name = "categorie_test.json"


@scenario('../features/buscar_categorias.feature', 'falha em buscar categoria inexistente')
def test_get_category_by_name_fail():
    pass

@given(parsers.cfparse( 'a categoria {category_name} não existe no banco de dados'))
def mock_category_service_response_fail(category_name: str):
    return {
        "category_name":category_name
    }

@when(parsers.cfparse('uma requisição GET for enviada para {req_url}'), target_fixture="context")
def send_get_category_request_fail(client, context, req_url: str):
    response = client.get(req_url, params={"file_name": db_file_name})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code_fail(context, status_code: str):
    assert context["response"].status_code == 404
    return context
