Feature: Login API

  Scenario: Login com sucesso
    Given que o loginService retorna um email "joao@email.com" e senha "123456"
    When eu envio uma requisição "GET" para "/login/joao/email.com/123456"
    Then eu recebo status code "200"
    And eu recebo o token "token"

  Scenario: Login com falha
    Given que o loginService retorna um email "joao@email.com" e senha "12345"
    When eu envio uma requisição "GET" para "/login/joao/email.com/12345"
    Then eu recebo status code "401"
    And eu recebo o token "null"

  Scenario: Login com campos vazios
    Given que o loginService retorna um email "" e senha ""
    When eu envio uma requisição "GET" para "/login//"
    Then eu recebo status code "400"
    And eu recebo o token "null"