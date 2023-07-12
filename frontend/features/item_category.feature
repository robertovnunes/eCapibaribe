Feature: Criar categorias de itens
    as a administrador
    I want criar categorias de itens
    so that os itens possam ser organizados em categorias

    Scenario: listando todas as categorias
        Given que estou na página de "categorias"
        Then eu vejo a categoria "Bebidas" na lista de categorias
        And eu vejo a categoria "Lanches" na lista de categorias
        And eu vejo a categoria "Sobremesas" na lista de categorias

    Scenario: listando categorias vazias
        Given que estou na página de "categorias"
        And eu vejo a lista de "categorias"
        And eu vejo a mensagem "Nenhuma categoria encontrada"

    Scenario: criando uma categoria
        Given que estou na página de "categorias"
        When eu clico em "Nova categoria"
        And eu preencho o campo "Nome" com "Bebidas"
        And eu preencho o campo "descrição da categoria" com "Liquidos alcoolicos ou não"
        And eu preencho o campo "palavras chaves" com "bebidas, bebidas alcoolicas, refrigerante"
        And eu adiciono "bebidas.png" como "imagem ilustrativa"
        And eu clico em "Salvar"
        Then eu vejo a mensagem "Categoria criada com sucesso"
        And eu vejo a categoria "Bebidas" na lista de categorias

    Scenario: criando uma categoria sem nome
        Given que estou na página de "categorias"
        When eu clico em "Nova categoria"
        And eu preencho o campo "Nome" com ""
        And eu clico em "Salvar"
        Then eu vejo a mensagem "Nome não pode ficar em branco"
        And eu continuo na página de "criação de categorias"

    Scenario: criando uma categoria com nome duplicado
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        When eu clico em "Nova categoria"
        And eu preencho o campo "Nome" com "Bebidas"
        And eu clico em "Salvar"
        Then eu vejo a mensagem "Nome já está em uso"
        And eu continuo na página de "criação de categorias"

    Scenario: Excluindo categoria vazia
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        When eu clico em "Excluir"
        Then eu vejo a mensagem "Categoria excluída com sucesso"
        And eu não vejo a categoria "Bebidas" na lista de categorias

    Scenario: Excluindo categoria com itens
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        And eu tenho um item "Coca-cola" na categoria "Bebidas"
        When eu clico em "Excluir"
        Then eu vejo a mensagem "Essa categoria possui itens, exclua ou desassocie os itens da categoria antes de excluí-la"
        And eu continuo na página de "categorias"
        And eu vejo a categoria "Bebidas" na lista de categorias

    Scenario: Excluindo categoria e desassociando itens
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        And eu tenho um item "coca-cola" na categoria "Bebidas"
        When eu clico em "Excluir"
        And eu clico em "Desassociar itens"
        Then eu vejo a mensagem "Categoria excluída com sucesso"
        And eu não vejo a categoria "Bebidas" na lista de categorias
        And eu ainda vejo o item "Coca-cola" na lista de itens

    Scenario: Excluindo categoria e excluindo itens
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        And eu tenho um item "Coca-cola" na categoria "Bebidas"
        When eu clico em "Excluir"
        And eu clico em "Excluir itens"
        Then eu vejo a mensagem "Categoria excluída com sucesso"
        And eu não vejo a categoria "Bebidas" na lista de categorias
        And eu não vejo o item "Coca-cola" na lista de itens

    Scenario: Editando nome de uma categoria
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        When eu clico em "Editar"
        And eu preencho o campo "Nome" com "Bebidas alcoolicas"
        And eu clico em "Salvar"
        Then eu vejo a mensagem "Categoria atualizada com sucesso"
        And eu vejo a categoria "Bebidas alcoolicas" na lista de categorias
        And eu não vejo a categoria "Bebidas" na lista de categorias

    Scenario: Editando descrição de uma categoria
        Given que estou na página de "categorias"
        And eu tenho uma categoria "Bebidas"
        When eu clico em "Editar"
        And eu preencho o campo "descrição da categoria" com "bebidas alcoolicas"
        And eu clico em "Salvar"
        Then eu vejo a mensagem "Categoria atualizada com sucesso"
        And eu vejo a categoria "Bebidas" na lista de categorias
        And eu vejo a descrição "bebidas alcoolicas" na lista de categorias