Feature: Registrar de Itens

    Scenario: Mostrar itens registrados
        Given que possuo items registrados
        When uma requisição GET for enviada para "/items"
        Then o status da resposta deve ser "200"
        And o arquivo da resposta deve possuir uma lista com os items registrados


    Scenario: Registrar item com sucesso
        Given o item de id  "89098" não está registrado
        When o usuario de cpf "123.456.789.10" registra o item
        And o sistema recebe a requisição POST para "/items" para registrar o Item 
        And com o id "89098"
        And "nome" "nome_teste"
        And "preco" "25.90"
        And "quantidade" "1"
        And "marca" "marca_teste"
        And "categoria" "categoria_teste"
        And "descricao" "desc_teste"
        And "imagem" "imagem.jpg"
        And "op_envio" "op_teste"
        And "palavrachave" "keyteste"
        Then o sistema registra o item
        And o sistema envia uma mensagem "Item registrado com sucesso!"

    Scenario: Falha ao registrar item com id repetido
        Given o item de id  "45654" está registrado
        When o usuario de cpf "123.456.789.10" registra o item
        And o sistema recebe a requisição POST para "/items" para registrar o Item
        And com o id "45654"
        And "nome" "nome_teste"
        And "preco" "25.90"
        And "quantidade" "1"
        And "marca" "marca_teste"
        And "categoria" "categoria_teste"
        And "descricao" "desc_teste"
        And "imagem" "imagem.jpg"
        And "op_envio" "op_teste"
        And "palavrachave" "keyteste"
        Then o sistema registra o item
        And o sistema envia uma mensagem de erro "Id ja está em uso!"

  
