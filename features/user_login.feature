Feature: Login de usuario
    As a user
    I want to login usin my username and password
    So I can use the system

    Scenario: login realizado com sucesso
        Given que eu estou na tela de login
        When eu preencho o campo username com "joao"
        And eu preencho o campo password com "123456"
        And eu clico no botão "Login"
        Then eu devo ver a mensagem "Login realizado com sucesso"
