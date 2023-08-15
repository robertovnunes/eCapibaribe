Feature: Cadastro de Usuários
        As a usuário
        I want me cadastrar
        So that posso salvar minhas informações para fazer meus pedidos

Scenario: Cadastro com sucesso
        Given usuário de e-mail “teste@email.com” não está cadastrado
        And usuário de CPF “123.456.789-10” não está cadastrado
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema cadastra o usuário
        And envia mensagem de sucesso "Cadastrada"
        
Scenario: Faltam campos obrigatórios - CPF
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “Faltam campos obrigatórios”

Scenario: Faltam campos obrigatórios - email
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”-
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “Faltam campos obrigatórios”

Scenario: Faltam campos obrigatórios - nome
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “Faltam campos obrigatórios”

Scenario: Faltam campos obrigatórios - sobrenome
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “Faltam campos obrigatórios”

Scenario: Faltam campos obrigatórios - senha
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        Then o sistema envia erro “Faltam campos obrigatórios”

Scenario: Cadastro com CPF já utilizado
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “CPF já cadastrado”

Scenario: Cadastro com CPF já inválido - 9 digitos
        Given o usuário de CPF “123.456.789-10” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-1”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “CPF já cadastrado”

Scenario: Cadastro com CPF já inválido - 12 digitos
        Given o usuário de CPF “123.456.789-101” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-1”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “CPF já cadastrado”

Scenario: Cadastro com e-mail já utilizado
        Given usuário de e-mail “teste@email.com” está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “teste@email.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “E-mail já cadastrado”

Scenario: Cadastro com e-mail inválido
        Given usuário de e-mail “teste@email.com” não está cadastrado no sistema
        When o sistema recebe o pedido para criar o usuário
        And com o nome com “teste”
        And com o e-mail com “testeemail.com”
        And com o CPF com “123.456.789-10”
        And com o sobrenome com “falha”
        And com a senha com  “0laMundo!”
        Then o sistema envia erro “E-mail já cadastrado”