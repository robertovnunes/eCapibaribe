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
