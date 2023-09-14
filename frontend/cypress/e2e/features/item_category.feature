Feature: Criar categorias de itens
  as a administrador
  I want criar categorias de itens
  so that os itens possam ser organizados em categorias

  Scenario: listando todas as categorias
    Given que estou na página de "listar categorias"
    And logado como "joao@email.com" e senha "123456"
    Then eu vejo a categoria "Bebidas" na lista de categorias
    And eu vejo a categoria "Lanches" na lista de categorias
    And eu vejo a categoria "Eletrodomésticos" na lista de categorias

  Scenario: listando categoria vazia
    Given que estou na página de "categorias"
    And eu vejo a lista de "categorias"
    And eu vejo a mensagem "Nenhuma categoria encontrada"
    And eu vejo a lista "categorias" vazia

  Scenario: criando uma categoria
    Given que estou na página de "categorias"
    When eu escolho "Nova categoria"
    And eu preencho o campo "Nome" com "Bebidas"
    And eu preencho o campo "descrição da categoria" com "Liquidos alcoolicos ou não"
    And eu preencho o campo "palavras chaves" com "bebidas, bebidas alcoolicas, refrigerante"
    And eu adiciono "bebidas.png" como "imagem ilustrativa"
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Categoria criada com sucesso"
    And eu vejo a categoria "Bebidas" na lista de categorias

  Scenario: criando uma categoria sem nome
    Given que estou na página de "categorias"
    When eu escolho "Nova categoria"
    And eu preencho o campo "Nome" com ""
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Nome não pode ficar em branco"
    And eu continuo na página de "criação de categorias"

  Scenario: criando uma categoria com nome duplicado
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Nova categoria"
    And eu preencho o campo "Nome" com "Bebidas"
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Nome já está em uso"
    And eu continuo na página de "criação de categorias"

  Scenario: Excluindo categoria vazia
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Excluir"
    Then eu vejo a mensagem "Categoria excluída com sucesso"
    And eu não vejo a categoria "Bebidas" na lista de categorias

  Scenario: Excluindo categoria com itens
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    And eu tenho um item "Coca-cola" na categoria "Bebidas"
    When eu escolho "Excluir"
    Then eu vejo a mensagem "Essa categoria possui itens, exclua ou desassocie os itens da categoria antes de excluí-la"
    And eu escolho "excluir itens"
    And eu continuo na página de "categorias"
    And eu vejo a mensagem "Categoria excluída com sucesso"
    And eu não vejo a categoria "Bebidas" na lista de categorias

  Scenario: Excluindo categoria e desassociando itens
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    And eu tenho um item "coca-cola" na categoria "Bebidas"
    When eu escolho "Excluir"
    Then eu vejo a mensagem "Essa categoria possui itens, exclua ou desassocie os itens da categoria antes de excluí-la"
    And eu escolho "Desassociar itens"
    Then eu vejo a mensagem "Categoria excluída com sucesso"
    And eu não vejo a categoria "Bebidas" na lista de categorias
    And eu ainda vejo o item "Coca-cola" na lista de itens

  Scenario: Excluindo categoria e excluindo itens
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    And eu tenho um item "Coca-cola" na categoria "Bebidas"
    When eu escolho "Excluir"
    And eu escolho "Excluir itens"
    Then eu vejo a mensagem "Categoria excluída com sucesso"
    And eu não vejo a categoria "Bebidas" na lista de categorias
    And eu não vejo o item "Coca-cola" na lista de itens

  Scenario: Cancelando exclusão de categoria
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Excluir"
    And eu escolho "Cancelar"
    Then eu continuo na página de "categorias"
    And eu vejo a categoria "Bebidas" na lista de categorias

  Scenario: Editando nome de uma categoria
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Editar"
    And eu preencho o campo "Nome" com "Bebidas alcoolicas"
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Categoria atualizada com sucesso"
    And eu vejo a categoria "Bebidas alcoolicas" na lista de categorias
    And eu não vejo a categoria "Bebidas" na lista de categorias

  Scenario: Editando descrição de uma categoria
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Editar"
    And eu preencho o campo "descrição da categoria" com "bebidas alcoolicas"
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Categoria atualizada com sucesso"
    And eu vejo a categoria "Bebidas" na lista de categorias
    And eu vejo a descrição "bebidas alcoolicas" na lista de categorias

  Scenario: Editando palavras chaves de uma categoria
    Given que estou na página de "categorias"
    And eu tenho uma categoria "Bebidas"
    When eu escolho "Editar"
    And eu preencho o campo "palavras chaves" com "bebidas, bebidas alcoolicas"
    And eu escolho "Salvar"
    Then eu vejo a mensagem "Categoria atualizada com sucesso"
    And eu vejo a categoria "Bebidas" na lista de categorias
    And eu vejo a palavra chave "bebidas, bebidas alcoolicas" na lista de categorias