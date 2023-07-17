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

Scenario: Atualizar cadastro
        Given o usuário está na página de “Atualizar cadastro”
        And usuário tem e-mail “teste@email.com” 
        And usuário tem CPF “123.456.789-10”
        And usuário tem o nome “teste”
        And usuário tem sobrenome “sucesso” 
        And usuário tem senha “0laMundo!”
        When o usuário preenche o nome com “atualizado”
        And o usuário seleciona a opção “Atualizar Cadastro”
        Then o usuário recebe uma mensagem “Cadastro atualizado com sucesso” 

Scenario: Remover cadastro
        Given o usuário está na página de “Perfil”
        And usuário tem e-mail “teste@email.com” 
        And usuário tem CPF “123.456.789-10”
        And usuário tem o nome “teste”
        And usuário tem sobrenome “sucesso” 
        And usuário tem senha “0laMundo!”
        When o usuário seleciona a opção “Deletar perfil”
        Then o usuário recebe uma mensagem “Perfil deletado com sucesso” 