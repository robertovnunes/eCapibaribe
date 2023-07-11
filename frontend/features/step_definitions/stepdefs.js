const assert = require('assert');
const { Given, When, Then } = require('@cucumber/cucumber');

const verifyCategoryExists = (category) => {
    if(category == 'Bebidas') {
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

  When('eu clico em {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
    if (string == 'Nova categoria') {
        if(verifyCategoryExists(string)) {
            return 'Categoria já existe';
        } else {
            return 'Nova categoria';
      }
    }
  });

  When('eu preencho o campo {string} com {string}', function (string, string2) {
    if(string == 'Nome' && string2 == '') {
      return 'Nome não pode ficar em branco';
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
    if(string == 'Bebidas') {
        return 'Bebidas';
    }
  });

  Then('eu continuo na página de {string}', function (string) {
    
    return string;
  });

