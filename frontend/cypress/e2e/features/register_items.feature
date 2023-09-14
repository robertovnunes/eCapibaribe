Feature: Registrar Items
     As a usuário
     I want registrar meus itens
     So that posso negociá-los

Scenario: Item registrado com sucesso
Given o usuário está na página de "/items/cadastro"
When o usuário preenche o id com "123", item_nome com "teste_name", preco com "11.90", quantidade com "1", marca com "marca_teste", categoria com "categoria_teste", descricao com "desc_teste", op_envio com "opção_teste", imagem com "imagemTeste" e o usuário seleciona a opção "Registraritem"
Then o usuário esta na pagina "/items/inventario"

Scenario: Falha por falta de campo obrigatorio
Given o usuário está na página de "/items/cadastro"
When o usuário preenche o item_nome com "teste_name", preco com "11.90", quantidade com "1", marca com "marca_teste", categoria com "categoria_teste", descricao com "desc_teste", op_envio com "opção_teste", imagem com "imagemTeste" e o usuário seleciona a opção "Registraritem"
Then o usuário recebe a mensagem "Faltam campos obrigatorios"

Scenario: Falha ao registrar item - id repetido
Given o usuário está na página de "/items/cadastro"
When o usuário preenche o id com "123", item_nome com "teste_name", preco com "11.90", quantidade com "1", marca com "marca_teste", categoria com "categoria_teste", descricao com "desc_teste", op_envio com "opção_teste", imagem com "imagemTeste" e o usuário seleciona a opção "Registraritem"
Then o usuário recebe a mensagem "Id já registrado"