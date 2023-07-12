Feature: Login de usuario
    As a user
    I want to login usin my username and password
    So I can use the system

    Scenario: login realizado com sucesso usando email
        Given que eu estou na tela de login
        When eu preencho o campo username com "joao@email.com"
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Login realizado com sucesso"

        Scenario: login realizado com sucesso usando cpf
        Given que eu estou na tela de login
        When eu preencho o campo username com "12345678900"
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Login realizado com sucesso"

    Scenario: login com campos usuario e senha vazios
        Given que eu estou na tela de login
        When eu preencho o campo username com ""
        And eu preencho o campo password com ""
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Preencha os campos username e password"

    Scenario: login com campo usuario vazio
        Given que eu estou na tela de login
        When eu preencho o campo username com ""
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Preencha o campo username"

    Scenario: login com campo senha vazio
        Given que eu estou na tela de login
        When eu preencho o campo username com "joao"
        And eu preencho o campo password com ""
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Preencha o campo password"

    Scenario: login com usuario e senha incorretos
        Given que eu estou na tela de login
        When eu preencho o campo username com "joao"
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Usuário e/ou senha incorretos"

    Scenario: login com usuario incorreto
        Given que eu estou na tela de login
        When eu preencho o campo username com "joao"
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Usuário e/ou senha incorretos"