import { Given, When, Then } from 'cypress-cucumber-preprocessor/steps'

Given('o usuário de CPF 123.456.789-10 está cadastrado no sistema e o usuário está na página de {string}', (page: string) => {
    cy.visit(page);
});

Given('o usuário está na página de {string}',
    (page: string) => {
      cy.visit(page, { timeout: 60000 });
    }
);

Given('usuário de e-mail teste@email.com está cadastrado no sistema e o usuário está na página de {string}',
    (page: string) => {
    cy.visit(page, { timeout: 60000 });
    }
);

When('o usuário preenche o nome com {string}, e-mail com {string}, CPF com {string}, sobrenome com {string}, senha com {string} e o usuário seleciona a opção "Concluir Cadastro"', 
    (nome: string, email: string, cpf: string, sobrenome: string, senha: string) => {
    cy.get('#nome').type(nome);
    cy.get('#email').type(email);
    cy.get('#cpf').type(cpf);
    cy.get('#sobrenome').type(sobrenome);
    cy.get('#senha').type(senha);
    cy.get('#registrar').click();
});

When('o usuário preenche o nome com {string}, e-mail com {string}, CPF com {string}, sobrenome com {string} e o usuário seleciona a opção "Concluir Cadastro"', 
    (nome: string, email: string, cpf: string, sobrenome: string, senha: string) => {
    cy.get('#nome').type(nome);
    cy.get('#email').type(email);
    cy.get('#cpf').type(cpf);
    cy.get('#sobrenome').type(sobrenome);
    cy.get('#registrar').click();
});


Then (
    'o usuário recebe uma mensagem {string}',
    (message: string) => {
      cy.get('#senha_errada').should('be.visible');
    }
  );

Then (
    'o usuário recebe uma mensagem {string}',
    (message: string) => {
        cy.get('#campo_obrigatorio').should('be.visible');
    }
);

Then('o usuário recebe uma mensagem {string}', (mensagemEsperada: string) => {
    cy.on('window:alert', (mensagemAlerta) => {
        expect(mensagemAlerta).to.equal(mensagemEsperada);
    });
});
