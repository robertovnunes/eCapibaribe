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





# cenários de lucas

Scenario: Deletar o usuário com sucesso
        Given o usuário de CPF “123.456.789-10” existe no sistema
        When uma requisição “DELETE” for enviada para “/user/delete/123.456.789-10/”
        Then o status da resposta deve ser “200”
        And o JSON da resposta deve conter o campo “mensagem” com o valor  “Usuário deletado com sucesso”

Scenario: Falha ao deletar usuário - usuário não existe
        Given o usuário de CPF “123.456.789-10” não existe no sistema
        When uma requisição “DELETE” for enviada para “/user/delete/123.456.789-10/”
        Then o status da resposta deve ser “404”
        And o JSON da resposta deve conter o campo “mensagem” com o valor “Usuário não existe”

Scenario: Modificar dados do usuário com sucesso
        Given o usuário de CPF “123.456.789-10” existe no sistema
        And o usuário tem e-mail “teste@email.com”
        And o usuário não tem telefone
        When uma requisição “PUT” for enviada para “/user/update” com o corpo da requisição que contém CPF “123.456.789-10”
        And contém e-mail “emailnovo@email.com”
        And contém telefone “12345678910”
        Then o status da resposta deve ser “200”
        And o usuário de CPF “123.456.789-10” deve ter o campo e-mail com o valor “emailnovo@email.com”
        And deve ter o campo telefone com o valor “12345678910”
        And o JSON da resposta deve conter mensagem “Dados modificados com sucesso.”

Scenario: Modificar dados com email inválido
        Given o usuário de CPF “123.456.789-10” existe no sistema
        And o usuário tem e-mail “teste@email.com”
        When uma requisição “PUT” for enviada para “/user/update” com o corpo da requisição que contém e-mail “emailnovo”
        Then o status da resposta deve ser 400
        And o usuário de CPF “123.456.789-10” deve ter o campo e-mail com o valor teste@email.com”
        And o JSON da resposta deve conter mensagem “Email inválido”

Scenario: Modificar dados com email inválido
        Given o usuário de CPF “123.456.789-10” existe no sistema
        And o usuário tem e-mail “teste@email.com”
        When uma requisição “PUT” for enviada para “/user/update” com o corpo da requisição que contém e-mail “emailnovo”
        Then o status da resposta deve ser 400
        And o usuário de CPF “123.456.789-10” deve ter o campo e-mail com o valor teste@email.com”
        And o JSON da resposta deve conter mensagem “Email inválido”

