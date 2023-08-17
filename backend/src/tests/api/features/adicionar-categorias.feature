Feature: Adicionar categorias no backend

  Scenario Outline: Adicionando Categoria
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o JSON
    """
    {
      "name": "<name>",
      "description": "<description>",
      "image": "<image>",
      "keywords": "<keywords>"
      "itens": "<items>"
    }
    """
    Then o status da resposta deve ser "200"
    And a categoria com id igual a "<id>" e nome igual a "<name>" esta no banco de dados

    Examples:
      | id | name   | description | image                         | keywords | items |
      | 4  | moveis | moveis      | https://picsum.photos/200/300 | Moveis   | []    |



