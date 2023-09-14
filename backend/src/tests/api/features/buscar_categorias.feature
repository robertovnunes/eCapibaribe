Feature: buscar categoria
    Scenario: Obter categoria por nome
        Given a categoria "bebidas" existe no banco de dados
        When uma requisição GET for enviada para "/categories/1"
        Then o status da resposta deve ser "200"
        And o corpo da resposta deve conter o id da categoria igual a "1"
        And o corpo da resposta deve conter o nome da categoria igual a "bebidas"
        And o corpo da resposta deve conter a descrição da categoria igual a "bebidas"
        And o corpo da resposta deve conter a url da imagem da categoria igual a "https://picsum.photos/200/300"
        And o corpo da resposta deve conter a lista de palavras-chave da categoria igual a "bebidas"
    
    Scenario: falha em buscar categoria inexistente
        Given a categoria "veiculos" não existe no banco de dados
        When uma requisição GET for enviada para "/categories/4"
        Then o status da resposta deve ser "404"
        