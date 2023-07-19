from pytest_bdd import scenario, given, when, then


@given('que o loginService retorna um email "joao@email.com" e senha "123456"')
def step_impl():
    raise NotImplementedError(u'STEP: Given que o loginService retorna um email "joao@email.com" e senha "123456"')


@when('eu envio uma requisição "GET" para "/login/joao@email.com/123456"')
def step_impl():
    raise NotImplementedError(u'STEP: When eu envio uma requisição "GET" para "/login/joao/email.com/123456"')


@then('eu recebo status code "200"')
def step_impl():
    raise NotImplementedError(u'STEP: Then eu recebo status code "200"')


@given('eu recebo o token "token"')
def step_impl():
    raise NotImplementedError(u'STEP: And eu recebo o token "token"')


@when('eu envio uma requisição "GET" para "/login/joao/email.com/12345"')
def step_impl():
    raise NotImplementedError(u'STEP: When eu envio uma requisição "GET" para "/login/joao/email.com/12345"')


@when('eu envio uma requisição "GET" para "/login//"')
def step_impl():
    raise NotImplementedError(u'STEP: When eu envio uma requisição "GET" para "/login//"')


@given('que o loginService retorna um email "joao@email.com" e senha "12345"')
def step_impl():
    raise NotImplementedError(u'STEP: Given que o loginService retorna um email "joao@email.com" e senha "12345"')


@then('eu recebo status code "401"')
def step_impl():
    raise NotImplementedError(u'STEP: Then eu recebo status code "401"')


@given('eu recebo o token "null"')
def step_impl():
    raise NotImplementedError(u'STEP: And eu recebo o token "null"')


@given('que o loginService retorna um email "" e senha ""')
def step_impl():
    raise NotImplementedError(u'STEP: Given que o loginService retorna um email "" e senha ""')


@then('eu recebo status code "400"')
def step_impl():
    raise NotImplementedError(u'STEP: Then eu recebo status code "400"')


@when('eu envio uma requisição "GET" para "/users/joao@email.com/123456"')
def step_impl():
    raise NotImplementedError(u'STEP: When eu envio uma requisição "GET" para "/users/joao@email.com/123456"')