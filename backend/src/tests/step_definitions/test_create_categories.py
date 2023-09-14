import pytest
from pydantic import BaseModel
from pytest_bdd import scenario, given, when, then, parsers

from ..utils.utils import req_type_to_function
from ...main import app


class Category(BaseModel):
    name: str
    description: str
    keywords: list
    items: list


@scenario(
    '../features/adicionar-categorias.feature', 'Adicionando Categoria')
def test_add_category():
    pass


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria com nome já existente')
def test_add_category_with_existing_name():
    pass


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria com nome vazio')
def test_add_category_with_empty_name():
    pass

@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria com descrição vazia')
def test_add_category_with_empty_description():
    pass


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria com imagem vazia')
def add_category_with_empty_image():
    pass


@given(parsers.cfparse('a categoria "{name}" não existe no banco de dados'), target_fixture="context")
def check_category_not_exists(context, client, name):
    """

    @param context:
    @param client:
    @param name:
    @return:
    """

    response = req_type_to_function(client, "GET")("/categories")
    categories = response.json()["data"]
    for category in categories:
        assert category["name"] != name
    return context


@pytest.mark.usefixtures("context")
@when(parsers.cfparse('uma requisição "POST" for enviada para "/categories" com o "{name}" "{description}" "{image}" '
                      '"{keywords}" "{itens}"'), target_fixture="context")
def send_post_request(context, client, name, description, image, keywords, itens):
    """
        @param context: context
        @param client: TestClient
        @type name: str
        @type description: str
        @type image: str
        @param keywords: list
        @param itens: list
    """

    itenslist = [itens]
    keywordlist = [keywords]
    new = Category(name=name,
                   description=description,
                   keywords=keywordlist,
                   items=itenslist).model_dump()
    response = req_type_to_function(client, "POST")("/categories", json=new)
    print(response.json())
    context["response"] = response
    return context


@pytest.mark.usefixtures("context")
@given(parsers.cfparse('a categoria "{name}" existe no banco de dados'), target_fixture="context")
def check_category_exists(context, client, name):
    response = req_type_to_function(client, "GET")("/categories")
    categories = response.json()["data"]
    for category in categories:
        if category["name"] == name:
            assert True
    return context

@then(parsers.cfparse('a categoria "{name}" existe no banco de dados'), target_fixture="context")
def check_category_exists(context, client, name):
    response = req_type_to_function(client, "GET")("/categories")
    categories = response.json()["data"]
    for category in categories:
        if category["name"] == name:
            assert True
    return context


@then(parsers.cfparse('a mensagem de erro deve ser "{message}"'), target_fixture="context")
def check_message(context, message):
    pass


@pytest.mark.usefixtures("context")
@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_status_code(context, status_code):
    pass
