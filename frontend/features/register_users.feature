Feature: Cadastro e manutenção de Usuários
        As a usuário
        I want me cadastrar e ter a opção de deletar minha conta e atualizar meus dados
        So that posso usar a loja


Scenario: Cadastro com CPF já utilizado
        Given o usuário de CPF “123.456.789-10” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o  CPF com “123.456.768-10”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “CPF já cadastrado”

Scenario: Cadastro com e-mail já utilizado
        Given usuário de e-mail “teste@email.com” está cadastrado no sistema
        And o usuário está na página de “Cadastro”
        When o usuário preenche o  e-mail com “teste@email.com”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “E-mail já cadastrado”

Scenario: Erro no cadastro - faltam campos obrigatórios
        Given o usuário está na página de “Cadastro”
        When o usuário preenche o nome com “teste”
        And o usuário preenche o e-mail com “teste@email.com”
        And o usuário preenche o CPF com “123.456.789-10”
        And o usuário preenche o sobrenome com “falha”
        And o usuário seleciona a opção “Concluir Cadastro”
        Then o usuário recebe uma mensagem “Campo obrigatório”