Feature: Cadastro de Usuários
        As a usuário
        I want me cadastrar
        So that posso salvar minhas informações para fazer meus pedidos

# cenários de lucas

Scenario: Deletar o usuário com sucesso
        Given o usuário de CPF "123.456.789-10" existe no sistema
        When uma requisição DELETE for enviada para "/users/delete/123.456.789-10/"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter o campo "message" com o valor "Usuário deletado com sucesso"

Scenario: Falha ao deletar usuário - usuário não existe
        Given o usuário de CPF "111.111.111-11" não existe no sistema
        When uma requisição DELETE for enviada para "/users/delete/111.111.111-11/"
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter o campo "detail" com o valor "Usuário não existe"

Scenario: Modificar dados do usuário com sucesso
        Given o usuário de CPF "123.456.789-10" existe no sistema
        And o usuário tem e-mail "teste@email.com"
        And o usuário não tem telefone
        When uma requisição "PUT" for enviada para "/users/update" com o corpo da requisição que contém CPF "123.456.789-10"
        And contém e-mail "emailnovo@email.com"
        And contém telefone "12345678910"
        Then o status da resposta deve ser "200"
        And o usuário de CPF "123.456.789-10" deve ter o campo e-mail com o valor "emailnovo@email.com"
        And deve ter o campo telefone com o valor "12345678910"
        And o JSON da resposta deve conter mensagem "Dados modificados com sucesso."

Scenario: Modificar dados com email inválido
        Given o usuário de CPF "123.456.789-10" existe no sistema
        And o usuário tem e-mail "teste@email.com"
        When uma requisição "PUT" for enviada para "/users/update" com o corpo da requisição que contém e-mail "emailnovo"
        Then o status da resposta deve ser 400
        And o usuário de CPF "123.456.789-10" deve ter o campo e-mail com o valor "teste@email.com"
        And o JSON da resposta deve conter mensagem "Email inválido"

#Scenario: Modificar dados com email inválido
#        Given o usuário de CPF "123.456.789-10" existe no sistema
#        And o usuário tem e-mail "teste@email.com"
#        When uma requisição "PUT" for enviada para "/user/update" com o corpo da requisição que contém e-mail "emailnovo"
#        Then o status da resposta deve ser 400
#        And o usuário de CPF "123.456.789-10" deve ter o campo e-mail com o valor "teste@email.com"
#        And o JSON da resposta deve conter mensagem "Email inválido"

