Feature: Adicionar categorias no backend
  As a administração do site
    I want to adicionar categorias no backend
    So that os usuarios possam ver as categorias no frontend

  Scenario Outline: Adicionando Categoria
    Given a categoria "<name>" não existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Examples:
        |name           |description   |image                        |keywords     |itens|
        | eletronicos   |  eletronicos |https://picsum.photos/200/300|[eletronicos]|[]   |
    Then o status da resposta deve ser "200"
    And a categoria "<name>" existe no banco de dados


  Scenario Outline: Adicionando Categoria com nome já existente
    Given a categoria "brinquedos" existe no banco de dados
    When uma requisição "POST" for enviada para "/categories" com o "<name>" "<description>" "<image>" "<keywords>" "<itens>"
    Examples:
        |name           |description   |image                        |keywords   |itens|
        | eletronicos   |  eletronicos |https://picsum.photos/200/300|eletronicos|[]   |
    Then o status da resposta deve ser "400"
    And a mensagem de erro deve ser "Categoria já existe"


