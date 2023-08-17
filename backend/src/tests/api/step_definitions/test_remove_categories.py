from pytest_bdd import scenario, given, when, then


@given('a categoria "bebidas" não existe mais no banco de dados')
def step_impl():
    raise NotImplementedError(u'STEP: And a categoria "bebidas" não existe mais no banco de dados')