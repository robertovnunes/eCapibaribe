Feature: Categorias API

  Scenario: Obter categoria por ID
    Given a categoria "bebidas" existe no banco de dados
    When uma requisição "GET" for enviada para "/categories/1"
    Then o status da resposta deve ser "200"
    And o corpo da resposta deve conter o id da categoria igual a "1"
    And o corpo da resposta deve conter o nome da categoria igual a "bebidas"
    And o corpo da resposta deve conter a descrição da categoria igual a "bebidas"
    And o corpo da resposta deve conter a url da imagem da categoria igual a "https://picsum.photos/200/300"
    And o corpo da resposta deve conter a lista de palavras-chave da categoria igual a "bebidas"

  Scenario Outline: Obter todas as categorias
    Given a categoria "bebidas" existe no banco de dados
    And a categoria "brinquedos" existe no banco de dados
    And a categoria "eletrônicos" existe no banco de dados
    When uma requisição "GET" for enviada para "/categories"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista com "3" categorias
    And a categoria com id igual a "<id>" e nome igual a <nome>
    And descrição igual a "<desc>"
    And imagem igual a "<image>"
    And palavras-chave igual a "<keywords>"
    And lista de itens igual a "<items>"

    Examples:
      | id | nome        | desc        | image                         | keywords    | items |
      | 1  | bebidas     | bebidas     | https://picsum.photos/200/300 | bebidas     | []    |
      | 2  | brinquedos  | brinquedos  | https://picsum.photos/200/300 | brinquedos  | []    |
      | 3  | eletronicos | eletronicos | https://picsum.photos/200/300 | eletronicos | []    |