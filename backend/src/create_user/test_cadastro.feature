Feature: Cadastro de Usuários
        As a usuário
        I want me cadastrar
        So that posso salvar minhas informações para fazer meus pedidos

Scenario: Cadastro com sucesso
        Given usuário de e-mail "teste_@email.com" não está cadastrado
        And usuário de CPF "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "teste_@email.com"
        And com o CPF com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!" 
        Then o sistema cadastra o usuário
        And envia mensagem de sucesso "Cadastro realizado com sucesso"
        
Scenario: Faltam campos obrigatórios
        Given usuário de e-mail "teste@email.com" não está cadastrado
        And usuário de CPF "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "teste@email.com"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "Todos os campos obrigatórios devem ser preenchidos"

Scenario: Cadastro com CPF já utilizado
        Given o usuário de CPF "12345678910" está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "teste@email.com"
        And com o CPF com "12345678910"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "CPF já cadastrado"

Scenario: Cadastro com CPF inválido
        Given o usuário de CPF "1234567891" não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "teste@email.com"
        And com o CPF com "1234567891"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "CPF inválido"

Scenario: Cadastro com e-mail já utilizado
        Given usuário de e-mail "teste@email.com" está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "teste@email.com"
        And com o CPF com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "E-mail já cadastrado"

Scenario: Cadastro com senha inválida
        Given usuário de e-mail "teste_@email.com" não está cadastrado no sistema
        And usuário de CPF "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "testeemail.com"
        And com o CPF com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0lamundo!"
        Then o sistema envia erro "Senha inválida! Falta uma letra maiúscula!"

Scenario: Cadastro com e-mail inválido
        Given usuário de e-mail "teste_@email.com" não está cadastrado no sistema
        And usuário de CPF "99999999999" não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com "teste"
        And com o e-mail com "testeemail.com"
        And com o CPF com "99999999999"
        And com o sobrenome com "falha"
        And com a senha com "0laMundo!"
        Then o sistema envia erro "E-mail inválido"