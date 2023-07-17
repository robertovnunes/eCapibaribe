Feature: Cadastro de itens

    As a usuário
	I want  cadastrar itens
	So that eu possa vendê-los

    Scenario: Item cadastrado com sucesso
        Given o usuário "123.456.789-10" está na página "cadastro de item"
        And o item de  id "45654" e nome "PortaRetrato" não está cadastrado
        When o usuário preenche os campos id "45654", nome "PortaRetrato", preço "11,99", quantidade "1", marca "imaginarium", categoria "foto", descrição "Contém 1 porta retrato com 1 suporte", imagem "ImagemDoProduto", opção de envio "Correio" 
        And o usuário seleciona a opção "Cadastrar item"
        Then o usuário de CPF "123.456.789-10" está na página "Inventário"
        And o usuário de CPF "123.456.678-10" visualiza o o item de ID "45654" e nome "PortaRetrato" na página "Inventário"
    
    Scenario: Falha no cadastro do item
        Given o usuário "123.456.789-10" está na página "cadastro de item"
        And o item de id "45654" e nome "PortaRetrato" não está cadastrado
        When o usuário preenche os campos nome "PortaRetrato", preço "11,99", quantidade "1", marca "imaginarium", categoria "foto", descrição "Contém 1 porta retrato com 1 suporte", imagem "ImagemDoProduto", opção de envio "Correio" 
        And o usuário seleciona a opção "Cadastrar item"
        Then o usuário recebe uma mensagem "Falha no cadastro, um campo obrigatorio nao preenchido"
        And o usuário permanece na página "cadastro de item"
