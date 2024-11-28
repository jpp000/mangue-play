describe('Teste de Depoimentos', () => {
  beforeEach(() => {
      cy.exec('del /f db.sqlite3'); 
      cy.exec('python manage.py migrate');
      cy.visit("http://127.0.0.1:8000");
      cy.get(".register").click();
      cy.get("#id_username").type("RafaelSerpa");
      cy.get("#id_email").type("rafaelserpa01@gmail.com");
      cy.get("#id_password1").type("rafaelserpa01");
      cy.get("#id_password2").type("rafaelserpa01");
      cy.get("#id_numero_telefone").type("81995750921");
      cy.get(".cadastrar").click();
      cy.wait(2000);
      cy.get(".username").type("RafaelSerpa");
      cy.get(".password").type("rafaelserpa01");
      cy.get(".login").click();
  });

  it('Deve permitir enviar um depoimento com sucesso', () => {
    cy.contains('Depoimentos').click(); 
    cy.get(".add-button").click();
    cy.get("#nome").type("Rafael Serpa");
    cy.get("#email").type("rafaelserpa01@gmail.com");
    cy.get("#telefone").type("(81) 99597-4215");
    cy.get("#texto").type("Estou adorando o site e a experiência com os brinquedos!");
    cy.get("button[type='submit']").click(); 
  });
  it('Não deve permitir enviar um depoimento sem preencher todos os campos', () => {
    cy.contains('Depoimentos').click(); 
    cy.get(".add-button").click();
    cy.get("#nome").type("Rafael Serpa");
    cy.get("#email").type("rafaelserpa01@gmail.com");
    cy.get("#texto").type("Estou adorando o site e a experiência com os brinquedos!");
    cy.get("button[type='submit']").click(); 
  });
});
