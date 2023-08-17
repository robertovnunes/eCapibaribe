from pytest_bdd import scenarios, given, when, then
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.impl.user_service import userService
from src.tests.api.utils.utils import get_response_categories_list, req_type_to_function

scenarios("../features/user-login.feature")


@given('que o userService retorna um email "{user_email}" e senha "{user_psword}"', target_fixture="context")
def mock_user_service_response(user_email: str, user_psword: str):
    userService.get_user = lambda id: HttpResponseModel(
        message=HTTPResponses.user_FOUND().message,
        status_code=HTTPResponses.user_FOUND().status_code,
        data={"email": user_email, "senha": user_psword})


@when('eu envio uma requisição "{req_type}" para "{req_url}"', target_fixture="context")
def send_get_user_response(client, context, req_type: str, req_url: str):
    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context


@then('eu recebo status code "{status_code}"', target_fixture="context")
def check_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context


@given('eu recebo o token "{token}"', target_fixture="context")
def check_response_token(context, token: str):
    assert context["response"].json()["token"] == token
    return context


@given('eu recebo o token "{token_login}"', target_fixture="context")
def check_respoonse_null_token(context, token_login: str):
    assert context["response"].json()["token"] == "null"
    return context


@then('eu recebo status code "{status_code}"', target_fixture="context")
def check_response_status_code(context, status_code: str):
    assert context["response"].status_code == int(status_code)
    return context

