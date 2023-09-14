import { Given, When, Then } from 'cypress-cucumber-preprocessor/steps'

Given('o usuário está na página de {string}',
    (page: string) => {
      cy.visit(page, { timeout: 60000 });
    }
);

When('o usuário preenche o id com {string}, item_nome com {string}, preco com {string}, quantidade com {string}, marca com {string}, categoria com {string}, descricao com {string}, op_envio com {string}, imagem com {string} e o usuário seleciona a opção "Registraritem"', 
    (id: string, nome_item: string, preco: string, quantidade: string, marca: string, categoria: string, descricao: string, op_envio: string, imagem: string) => {
    cy.get('#item_id').type(id);
    cy.get('#item_nome').type(nome_item);
    cy.get('#item_price').type(preco);
    cy.get('#quantidade').type(quantidade);
    cy.get('#marca').type(marca);
    cy.get('#categoria').type(categoria);
    cy.get('#descricao').type(descricao);
    cy.get('#op_envio').type(op_envio);
    cy.get('#RegistrarItem').click();
});

When('o usuário preenche o item_nome com {string}, preco com {string}, quantidade com {string}, marca com {string}, categoria com {string}, descricao com {string}, op_envio com {string}, imagem com {string} e o usuário seleciona a opção "Registraritem"', 
    (id: string, nome_item: string, preco: string, quantidade: string, marca: string, categoria: string, descricao: string, op_envio: string, imagem: string) => {
    cy.get('#item_id').type(id);
    cy.get('#item_nome').type(nome_item);
    cy.get('#item_price').type(preco);
    cy.get('#quantidade').type(quantidade);
    cy.get('#marca').type(marca);
    cy.get('#categoria').type(categoria);
    cy.get('#descricao').type(descricao);
    cy.get('#op_envio').type(op_envio);
    cy.get('#RegistrarItem').click();
});


Then ('o usuário esta na pagina {string}',
    (page: string) => {
        cy.visit(page, { timeout: 60000 });
      }
  );

Then('o usuário recebe a mensagem {string}', (mensagemEsperada: string) => {
    cy.on('window:alert', (mensagemAlerta) => {
        expect(mensagemAlerta).to.equal(mensagemEsperada);
    });
});