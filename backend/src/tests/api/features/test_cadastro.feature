Feature: Cadastro de Usuários
        As a usuário
        I want me cadastrar
        So that posso salvar minhas informações para fazer meus pedidos

Scenario: Cadastro com sucesso
        Given usuário de email "teste_@email.com" não está cadastrado
        And usuário de cpf "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "teste_@email.com"
        And com o cpf com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!" 
        Then o sistema cadastra o usuário
        And envia mensagem de sucesso "Cadastro realizado com sucesso"
        
Scenario: Faltam campos obrigatórios
        Given usuário de email "teste@email.com" não está cadastrado
        And usuário de cpf "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "teste@email.com"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "Todos os campos obrigatórios devem ser preenchidos"

Scenario: Cadastro com cpf já utilizado
        Given o usuário de cpf "12345678910" está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "teste@email.com"
        And com o cpf com "12345678910"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "cpf já cadastrado"

Scenario: Cadastro com cpf inválido
        Given o usuário de cpf "1234567891" não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "teste@email.com"
        And com o cpf com "1234567891"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "cpf inválido"

Scenario: Cadastro com email já utilizado
        Given usuário de email "teste@email.com" está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "teste@email.com"
        And com o cpf com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "email já cadastrado"

Scenario: Cadastro com senha inválida
        Given usuário de email "teste_@email.com" não está cadastrado no sistema
        And usuário de cpf "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "testeemail.com"
        And com o cpf com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0lamundo!"
        Then o sistema envia erro "Senha inválida! Falta uma letra maiúscula!"

Scenario: Cadastro com email inválido
        Given usuário de email "teste_@email.com" não está cadastrado no sistema
        And usuário de cpf "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o email com "testeemail.com"
        And com o cpf com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "email inválido"