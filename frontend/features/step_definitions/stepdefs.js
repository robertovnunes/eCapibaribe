const assert = require('assert');
const { Given, When, Then } = require('@cucumber/cucumber');

const verifyCategoryExists = (category) => {
    if(category === 'Bebidas') {
        return true;
    }
    else {
      return false;
    }
}

Given('que estou na página de {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
      return 'Categorias';
  });

  Given('eu tenho uma categoria {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
    return 'bebidas';
  });

  When('eu escolho {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
    if (string === 'Nova categoria') {
        if(verifyCategoryExists(string)) {
            return 'Categoria já existe';
        } else {
            return 'Nova categoria';
      }
    }
  });

  When('eu preencho o campo {string} com {string}', function (string, string2) {
    if(string === 'Nome' && string2 === '') {
      return 'Nome não pode ficar em branco';
    } else {
      return '';
    }
  });

   When('eu adiciono {string} como {string}', function (string, string2) {
           // Write code here that turns the phrase above into concrete actions
           if(string === '' || string2 === '') {
      return 'Imagem não pode ficar em branco';
    } else {
      return '';
    }
   });


  Then('eu vejo a mensagem {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
    return 'Categoria criada com sucesso';
  });

  Then('eu vejo a categoria {string} na lista de categorias', function (string) {
    // Write code here that turns the phrase above into concrete actions
    if(string === 'Bebidas') {
        return 'Bebidas';
    }
  });

  Then('eu continuo na página de {string}', function (string) {
    
    return string;
  });

Then('eu não vejo a categoria {string} na lista de categorias', function (string) {
    return 'Categoria não existe';
});

Then('eu ainda vejo o item {string} na lista de itens', function (string) {
    return "{string} está na lista de itens";
});
Then('eu não vejo o item {string} na lista de itens', function (string) {
    return 'Item não existe';
});
Given('eu tenho um item {string} na categoria "Bebidas"', function (string) {

});
Given('eu vejo a lista de {string}', function (string) {
    return 'Lista de itens vazia';
});
Then(/^eu vejo a descrição "([^"]*)" na lista de categorias$/, function () {
    return '';
});
Given(/^que eu estou na tela de login$/, function () {

});
When(/^eu preencho o campo username com "([^"]*)"$/, function () {

});
When(/^eu preencho o campo password com "([^"]*)"$/, function () {

});
When(/^eu escolho no botão "([^"]*)"$/, function () {

});
Then(/^eu devo ver a mensagem "([^"]*)"$/, function () {

});
Then(/^eu devo ser redirecionado para a pagina "([^"]*)"$/, function () {

});
Given(/^logado como "([^"]*)" e senha "([^"]*)"$/, function () {

});
Given(/^eu vejo a lista "([^"]*)" vazia$/, function () {

});
Given(/^que eu estou na tela "([^"]*)"$/, function () {

});
Then(/^eu escolho "([^"]*)"$/, function () {

});
Then(/^eu vejo a palavra chave "([^"]*)" na lista de categorias$/, function () {

});