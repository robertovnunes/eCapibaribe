import json

from pytest_bdd import scenario, given, when, then, parsers


from ..utils.utils import req_type_to_function

url = "https://127.0.0.1/8000/categories"


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria')
def test_add_category():
    pass


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria com nome já existente')
def test_add_category_with_existing_name():
    pass


@given(parsers.cfparse('a categoria "{name}" não existe no banco de dados'), target_fixture="context")
def check_category_not_exists(context, client, name):
    response = req_type_to_function(client, "GET")
    print(response)



@when(parsers.cfparse('uma requisição "POST" for enviada para "/categories" com o "{name}" "{description}" "{image}" '
                      '"{keywords}" "{itens}"'), target_fixture="context")
def send_post_request(client, context, name, description, image, keywords, itens):
    """


    @param client: object
    @param context: object
    @type name: str
    @type description: str
    @type image: str
    @param keywords: list
    @param itens: list
    """

    newcat = {"name": name, "description": description, "image": image, "keywords": keywords, "itens": itens}
    response = req_type_to_function(client, "POST")(url, json=newcat)
    print(response)
    return context


@given(parsers.cfparse('a categoria "{name}" existe no banco de dados'), target_fixture="context")
def check_category_exists(client, name):
    categories = req_type_to_function(client, "GET")
    print(categories)


@then(parsers.cfparse('a mensagem de erro deve ser "{message}"'), target_fixture="context")
def check_message(context, client, message):
    response = context["response"]
    assert response.json()["message"] == message


@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_status_code(context, client, status_code):
    response = context["response"]
    assert response.status_code == int(status_code)
