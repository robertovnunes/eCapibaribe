Feature: Adicionar categorias no backend
  As a administração do site
    I want to adicionar categorias no backend
    So that os usuarios possam ver as categorias no frontend

  Scenario Outline: Adicionando Categoria
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Then o status da resposta deve ser "200"
    And a categoria "<name>" existe no banco de dados
    Examples:
      | name   | description | image                         | keywords      | itens |
      | comida | eletronicos | https://picsum.photos/200/300 | [eletronicos] | null  |


  Scenario Outline: Adicionando Categoria com nome já existente
    Given a categoria "<name>" existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Then o status da resposta deve ser "400"
    And a mensagem de erro deve ser "Category already exists"
    Examples:
      | name       | description | image                         | keywords     | itens |
      | brinquedos | brinquedos  | https://picsum.photos/200/300 | [brinquedos] | null  |


  Scenario Outline: Adicionando Categoria com nome vazio
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Then o status da resposta deve ser "400"
    And a mensagem de erro deve ser "Category name cannot be empty"
    Examples:
      | name | description | image                         | keywords     | itens |
      |      | brinquedos  | https://picsum.photos/200/300 | [brinquedos] | null  |


  Scenario Outline: Adicionando Categoria com descrição vazia
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Then o status da resposta deve ser "400"
    And a mensagem de erro deve ser "Category description cannot be empty"
    Examples:
      | name   | description | image                         | keywords     | itens |
      | comida |             | https://picsum.photos/200/300 | [brinquedos] | null  |


  Scenario Outline: Adicionando Categoria com imagem vazia
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Then o status da resposta deve ser "400"
    And a mensagem de erro deve ser "Category image cannot be empty"
    Examples:
      | name   | description | image | keywords | itens |
      | comida | comida      |       | [comida] | null  |