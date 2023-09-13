const { Given, When, Then } = require("cypress-cucumber-preprocessor");

Given("o usuário de CPF \"123.456.789-10\" está cadastrado no sistema e o usuário está na página de \"Cadastro\"", () => {
cy.visit("/users/register");
});

When("o usuário preenche o nome com {string}", (nome) => {
cy.get("#nome").type(nome);
});

And("o usuário preenche o e-mail com {string}", (email) => {
    cy.get("#email").type(email);
});

And("o usuário preenche o CPF com {string}", (cpf) => {
    cy.get("#cpf").type(cpf);
});

And("o usuário preenche o sobrenome com {string}", (sobrenome) => {
    cy.get("#sobrenome").type(sobrenome);
});

And("o usuário preenche a senha com {string}", (senha) => {
    cy.get("#senha").type(senha);
});

And("o usuário seleciona a opção \"Concluir Cadastro\"", () => {
    cy.get("#registrar").click();
});

Then("o usuário recebe uma mensagem {string}", (mensagemEsperada) => {
    cy.on("window:alert", (mensagemAlerta) => {
        expect(mensagemAlerta).to.equal(mensagemEsperada);
    });
});