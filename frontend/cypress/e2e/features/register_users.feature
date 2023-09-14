Feature: Cadastro de Usuários
     As a usuário
     I want me cadastrar
     So that posso salvar minhas informações para fazer meus pedidos

Scenario: Cadastro com senha inválida - sem caractere especial
Given o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste@email.com", CPF com "123.456.789-101", sobrenome com "falha", senha com "0laMundo" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe uma mensagem "A senha deve ter pelo menos 6 caracteres, 1 caractere especial, 1 letra maiúscula, 1 letra minúscula e 1 dígito."

Scenario: Cadastro com CPF já utilizado
Given o usuário de CPF 123.456.789-10 está cadastrado no sistema e o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste324@email.com", CPF com "123.456.789-10", sobrenome com "falha", senha com "0laMundo!" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe um alerta "CPF já cadastrado"

Scenario: Cadastro com CPF inválido
Given o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste@email.com", CPF com "123.456.789-101", sobrenome com "falha", senha com "0laMundo!" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe um alerta "CPF inválido"

Scenario: Cadastro com e-mail já utilizado
Given usuário de e-mail teste@email.com está cadastrado no sistema e o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste@email.com", CPF com "99999999999", sobrenome com "falha", senha com "OlaMundo!" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe um alerta "Email já cadastrado"

Scenario: Erro no cadastro - faltam campos obrigatórios
Given o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste@email.com", CPF com "123.456.789-10", sobrenome com "falha" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe uma mensagem "Todos os campos obrigatórios devem ser preenchidos"

Scenario: Cadastro com sucesso
Given o usuário está na página de "/users/register"
When o usuário preenche o nome com "teste", e-mail com "teste@email.com", CPF com "123.456.789-10", sobrenome com "sucesso", senha com "0laMundo!" e o usuário seleciona a opção "Concluir Cadastro"
Then o usuário recebe um alerta "Cadastro realizado com sucesso"
