# Created by roberto at 17/08/2023
Feature: Remover categoria do banco de dados

  Scenario: Removendo categoria
    Given a categoria "bebidas" existe no banco de dados
    When uma requisição "DELETE" for enviada para "/categories/1"
    Then o status da resposta deve ser "200"
    And a categoria "bebidas" não existe mais no banco de dados