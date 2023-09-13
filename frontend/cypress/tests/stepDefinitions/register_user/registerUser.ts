import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor"

Given("o usuário de CPF \"123.456.789-10\" está cadastrado no sistema e o usuário está na página de \"Cadastro\"", () => {
cy.visit("/users/register");
});

