from pytest_bdd import scenario, given, when, then


@scenario('../features/adicionar-categorias.feature', 'Adicionando Categoria')
@given('a categoria "<name>" não existe no banco de dados')
def check_category_not_exists(name):
    raise NotImplementedError(u'STEP: And a categoria "<name>" não existe no banco de dados')


@when('uma requisição "POST" for enviada para "/categories" com o JSON')
def send_post_request():
    raise NotImplementedError(u'STEP: When uma requisição "POST" for enviada para "/categories" com o JSON')
