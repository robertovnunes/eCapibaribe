Feature: Cadastro e Manutenção de itens (Inserir, Remover, Atualizar)

	As vendedor
	I want to conseguir registrar, atualizar e remover itens
	so that  eu possa  manusear meus itens e vendê-los

    Scenario: Item cadastrado com sucesso
        Given o usuário "123.456.789-10" está na página "cadastro de item"
        And o item de  id "45654" e nome "PortaRetrato" não está cadastrado
        When o usuário preenche os campos id "45654"
        And nome "PortaRetrato"
        And preço "11,99"
        And quantidade "1"
        And marca "imaginarium"
        And categoria "foto"
        And descrição "Contém 1 porta retrato com 1 suporte"
        And imagem "ImagemDoProduto"
        And opção de envio "Correio"  
        And o usuário seleciona a opção "Cadastrar item"
        Then o usuário de CPF "123.456.789-10" está na página "Inventário"
        And o usuário de CPF "123.456.678-10" visualiza o o item de ID "45654" e nome "PortaRetrato" na página "Inventário"
    
    Scenario: Falha no cadastro do item por nao preenchimeto de campo obrigatorio
        Given o usuário "123.456.789-10" está na página "cadastro de item"
        And o item de id "45654" e nome "PortaRetrato" não está cadastrado
        When o usuário preenche o nome "PortaRetrato"
        And preço "11,99"
        And quantidade "1"
        And marca "imaginarium"
        And categoria "foto"
        And descrição "Contém 1 porta retrato com 1 suporte"
        And imagem "ImagemDoProduto"
        And opção de envio "Correio"
        And palavra-chave "retrato" 
        And o usuário seleciona a opção "Cadastrar item"
        Then o usuário recebe uma mensagem "Falha no cadastro, um campo obrigatorio nao preenchido"
        And o usuário permanece na página "cadastro de item"
        And o usuário visualiza o campo "ID" , que está vazio, destacado

    Scenario: Cadastrar item repetido
        Given o usuário "123.456.789-10" está na página "cadastro de item"
        And o item de id "45654" e nome "PortaRetrato" está na página "Inventário"
        When o usuário preenche os campos id "45654"
        And nome "PortaRetrato"
        And preço "11,99"
        And quantidade "1"
        And marca "imaginarium"
        And categoria "foto"
        And descrição "Contém 1 porta retrato com 1 suporte"
        And imagem "ImagemDoProduto"
        And opção de envio "Correio"   
        And o usuário seleciona a opção "Cadastrar item"
        Then o usuário recebe uma mensagem "Este item já está cadastrado em seu inventário"
        And o usuário permanece na página "cadastro de item"

    Scenario: Remover item
        Given o usuário de cpf "123.456.789-10" está na página “Inventário”
        And o item com nome “PortaRetratoNovo” e id "45654" está na página “Inventário” 
        When o usuário seleciona “Remover item”
        And  seleciona “Confirmar”  
        Then o usuário visualiza a mensagem “O item foi removido com sucesso!”
        And o usuario permanece na pagina “Inventario” 
        And o item com nome “PortaRetratoNovo” e id “45654” não é visualizado

    Scenario: Atualização de item
        Given o usuario de cpf "123.456.789-10" está na página “Inventário”
        And o item com nome “PortaRetrato” e id "45654" está na página “inventário”
        When o usuario seleciona “Atualizar item” 
        And altera o campos nome “PortaRetrato” para o nome “PortaRetratoNovo” 
        And  seleciona “Salvar alterações”
        Then o usuario recebe a mensagem “Alterações salvas!” 
        And o usuario permanece na página “Inventário” 
        And o item com o nome “PortaRetratoNovo” e id “45654” está na página “Inventário”
