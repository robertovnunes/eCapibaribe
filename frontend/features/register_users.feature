Feature: Cadastro de Usuários
        As a usuário
        I want me cadastrar
        So that posso salvar minhas informações para fazer meus pedidos


Scenario: Cadastro com CPF já utilizado
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-10”
        And o usuário preenche o sobrenome com “falha”
        And o usuário preenche a senha com  “0laMundo!”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “CPF já cadastrado”

Scenario: Cadastro com CPF inválido
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-101”
        And o usuário preenche o sobrenome com “falha”
        And o usuário preenche a senha com  “0laMundo!”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “CPF já cadastrado”

Scenario: Cadastro com senha inválida - sem caractere especial
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-101”
        And o usuário preenche o sobrenome com “falha”
        And o usuário preenche a senha com  “0laMundo”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “Senha inválida! Falta caractere especial”

Scenario: Cadastro com senha inválida - sem número
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-101”
        And o usuário preenche o sobrenome com “falha”
        And o usuário preenche a senha com  “OlaMundo!”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “Senha inválida! Falta número!”

Scenario: Cadastro com e-mail já utilizado
        Given usuário de e-mail “teste@email.com” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-10”
        And o usuário preenche o sobrenome com “falha”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “E-mail já cadastrado”

Scenario: Erro no cadastro - faltam campos obrigatórios
        Given o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-10”
        And o usuário preenche o sobrenome com “falha”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem "Todos os campos obrigatórios devem ser preenchidos"

Scenario: Cadastro com sucesso
        Given o usuário está na página de “Cadastro”
        And usuário de e-mail “teste@email.com” 
        And usuário de CPF “123.456.789-10” não está cadastrado
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-10”
        And o usuário preenche o sobrenome com “sucesso”
        And o usuário preenche a senha com  “0laMundo!”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “Cadastro realizado com sucesso” 
        And o usuário é redirecionado para a página de "Login"

