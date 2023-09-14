import { Given, When, Then } from 'cypress-cucumber-preprocessor/steps'

Given('o usuário está na página de {string} e clica em "edit" no item de id {string}',
    (page: string, id: string) => {
      cy.visit(page, { timeout: 60000 });
      cy.get('mdc-icon-button mat-mdc-icon-button mat-primary mat-mdc-button-base').contains("onEdit(element.item_id)");
      cy.get('#item_id').type(id);
    }
);

When('o usuário altera os campos preço {string} e quantidade {string} e clica em "Editar"', 
    (preco: string, quantidade: string) => {
    cy.get('#item_price').type(preco);
    cy.get('#quantidade').type(quantidade);
    cy.get('#Editar').click();
});

Then ('o usuário recebe um alerta sobre a alteração e retorna para a pagina {string} com o item editado',
    (page: string) => {
        cy.visit(page, { timeout: 60000 });
      }
);

////////////////////////////////

Given('o usuário está na página de {string}',
    (page: string) => {
      cy.visit(page, { timeout: 60000 });
    }
);

When('o usuário clica em "deletar" e logo após clica em "Ok"', 
    () => {
    cy.get('Editar').contains("onDelete(element.item_id)");
    cy.get('mat-button [mat-dialog-close]').contains('true').click();
});

Then ('o usuário recebe uma mensagem e permanece na página {string}',
    (page: string) => {
        cy.visit(page, { timeout: 60000 });
      }
);

////////////////////////////////

When('o usuário clica em "deletar" e logo após clica em "No Thanks"', 
    () => {
    cy.get('Editar').contains("onDelete(element.item_id)");
    cy.get('mat-button (click)').contains('onNoClick()').click();
});

Then ('o usuário permanece na paǵina {string} e o item se mantém',
    (page: string) => {
        cy.visit(page, { timeout: 60000 });
      }
);
