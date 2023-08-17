Feature: Manutenção de item

    Scenario: Atualizar Item
        Given o item id "854256" está registrado
        When uma requisição PUT for realizada na rota "/items/update" com o corpo da requisição com o campo "item_price"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter a mensagem "Informações do item id '854256' alteradas com sucesso!"
        And o JSON da resposta deve conter o campo "item_price" do item id "854256" com valor alterado

    Scenario: Remover Item
        Given o item id "45754" está no registrado
        When uma requisição DELETE for realizada na rota "/items/delete" com o id do item "45754" no corpo da requisição
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter o campo "msg" do item id "45754"



