import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor"

When("o usuário preenche o nome com {string} e o usuário preenche o e-mail com {string} e o usuário preenche o CPF com {string} e o usuário preenche o sobrenome com {string} e o usuário preenche a senha com {string} e o usuário seleciona a opção \"Concluir Cadastro\"", 
    (nome: string, email: string, cpf: string, sobrenome: string, senha: string) => {
    cy.get("#nome").type(nome);
    cy.get("#email").type(email);
    cy.get("#cpf").type(cpf);
    cy.get("#sobrenome").type(sobrenome);
    cy.get("#senha").type(senha);
    cy.get("#registrar").click();
});

Then("o usuário recebe uma mensagem {string}", (mensagemEsperada: string) => {
    cy.on("window:alert", (mensagemAlerta) => {
        expect(mensagemAlerta).to.equal(mensagemEsperada);
    });
});