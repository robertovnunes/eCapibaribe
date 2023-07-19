Feature: Categorias API

  Scenario: Obter categoria por ID
    Given o categoryService retorna uma categoria com id "123"
    And a categoria não existe no banco de dados
    When uma requisição "GET" for enviada para "/categorias/123"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve conter id "123" e nome "Bebidas"

  Scenario: Adicionando categoria
    Given não existe a categoria "bebidas" no banco de dados
    When uma requisição "POST" for enviada para "/categorias" com o JSON:
    """
    {
      "nome": "Bebidas",
      "descricao": "Bebidas em geral",
      "imagem": "http://picsum.photos/200/300",
      "keywords": ["bebidas", "refrigerantes", "cervejas"]
    }
    """
    Then o status da resposta deve ser "201"
    And o JSON da resposta deve conter id "123" e nome "Bebidas"

  

  Scenario: Obter todas as categorias
    Given o categoryService retorna uma lista de itens
    When uma requisição "GET" for enviada para "/categorias"
    Then o status da resposta deve ser "200"
    And o JSON da resposta deve ser uma lista de itens
    And a categoria com id "123" e nome "Bebidas" está na lista
    And a categoria com id "456" e nome "Brinquedos" está na lista

  Scenario: Obter categoria por ID inexistente
    Given o categoryService não retorna um categoria com id "123"
    When uma requisição "GET" for enviada para "/categorias/123"
    Then o status da resposta deve ser "404"
