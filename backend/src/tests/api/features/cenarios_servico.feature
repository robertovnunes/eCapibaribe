Feature: Registrar de Itens

    Scenario: Mostrar itens registrados
        Given que possuo items registrados
        When uma requisição "GET"  for enviada para "/items"
        Then o status da resposta deve ser "200"
        And o arquivo da resposta deve possuir uma lista com todos os items registrados


    Scenario: Registrar item com sucesso
        Given o item de id  "89098" não está registrado
        When o sistema recebe a requisição para registrar o item com item_id "89098"
        And nome "nome_teste"
        And preço "25.90"
        And quantidade "1"
        And marca "marca_teste"
        And categoria "categoria_teste"
        And descricao "desc_teste"
        And imagem "imagem.jpg"
        And op_envio "op_teste"
        And palavrachave "keyteste"
        Then o sistema registra o item
        And envia mensagem de sucesso "Item registrado com sucesso"

    Scenario: Falha ao registrar item com id repetido
        Given o item de id  "89098" está registrado
        When o sistema recebe a requisição para registrar o item com item_id "89098"
        And nome "nome_teste"
        And preço "25.90"
        And quantidade "1"
        And marca "marca_teste"
        And categoria "categoria_teste"
        And descricao "desc_teste"
        And imagem "imagem.jpg"
        And op_envio "op_teste"
        And palavrachave "keyteste"
        Then o sistema envia o erro "Item_id ja registrado"


"""Scenario: Obter todos os itens
    When eu faço uma requisição GET para "/items"
    Then a resposta deve ter o status code 200
    And a resposta deve ser uma lista de itens


    Scenario: Registrar o item com sucesso
        Given o item de id  "89098" não está registrado
        When uma requisição "POST" for enviada para "/items" com o arquivo: "{"item_id": 89098, 
                                                                            "item_nome":"nome_teste", 
                                                                            "item_price": 24.35, 
                                                                            "quantidade": 1, 
                                                                            "marca": "marca_teste", 
                                                                            "categoria": "categoria_teste", 
                                                                            "descricao": "desc_teste",  
                                                                            "imagem": "imagem.jpg", 
                                                                            "op_envio": "op_teste",
                                                                            "palavrachave": "keyteste"
                                                                        }"
        Then o status da resposta deve ser "200"
        And o usuario recebe uma mensagem  "Item registrado com sucesso"
        And o item aparece no banco de dados
    

    Scenario: Falha ao registrar o item com id repetido
        Given o item de id  "89098"  está registrado
        When uma requisição "POST" for enviada para "/items" com o arquivo:{
                                                                            "item_id": 89098, 
                                                                            "item_nome":"nome_teste", 
                                                                            "item_price": 24.35, 
                                                                            "quantidade": 1, 
                                                                            "marca": "marca_teste", 
                                                                            "categoria": "categoria_teste", 
                                                                            "descricao": "desc_teste",  
                                                                            "imagem": "imagem.jpg", 
                                                                            "op_envio": "op_teste"
                                                                        }
        Then o status da resposta deve ser "409"
        And o sistema envia uma mensagem de erro "Falha ao registrar, id ja existe""""
  
