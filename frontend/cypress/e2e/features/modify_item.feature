Feature: Modificar items
     As a usuário
     I want modificar meus itens
     So that posso alterar suas informações

Scenario: Alteração bem sucedida
Given o usuário está na página de "/items/inventario" e clica em "edit" no item de id "123"
When o usuário altera os campos preço "30.64" e quantidade "2" e clica em "Editar"
Then o usuário recebe um alerta sobre a alteração e retorna para a pagina "/items/inventario" com o item editado

Scenario: Escolha por não deletar item
Given o usuário está na página de "/items/inventario"
When o usuário clica em "deletar" e logo após clica em "No Thanks"
Then o usuário permanece na paǵina "/items/inventario" e o item se mantém

Scenario: Escolha por deletar item
Given o usuário está na página de "/items/inventario"
When o usuário clica em "deletar" e logo após clica em "Ok"
Then o usuário recebe uma mensagem e permanece na página "/items/inventario"