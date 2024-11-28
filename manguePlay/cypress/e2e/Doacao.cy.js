describe('Doacao e2e tests', () => {
  const adminData = {
    username: "admin",
    email: "admin@example.com",
    password: "123",
    numeroTelefone: "123456789",
    isAdmin: true,
  };
  beforeEach(() => {
    cy.exec('rm -f db.sqlite3'); 
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

  it('Doacao test', () => {
    cy.contains('Doação e Coleta de Materiais').click();
    cy.get('.button').should('contain', 'Desejo Doar').click();
    cy.get('#nome_doador').type('Rafael Serpa');
    cy.get('#contato').type('(81) 99999-4215');
    cy.get('#local').type('Rua do Mangue, 123');
    cy.get('#data').type('2024-12-01'); 
    cy.get('#hora_inicio').type('09:00');
    cy.get('#hora_fim').type('12:00');
    cy.get('#observacoes').type('Doação de brinquedos e roupas recicláveis.');
    cy.get('button[type="submit"]').click();

    cy.visit("http://127.0.0.1:8000/cadastro");

      cy.get('input[name="username"]').type(adminData.username);
      cy.get('input[name="email"]').type(adminData.email);
      cy.get('input[name="password1"]').type(adminData.password);
      cy.get('input[name="password2"]').type(adminData.password);
      cy.get('input[name="numero_telefone"]').type(adminData.numeroTelefone);

      cy.get('input[name="is_admin"]').check();

      cy.get('button[type="submit"]').click();

      cy.visit("http://127.0.0.1:8000/login");

      cy.get('input[name="username"]').type(adminData.username);
      cy.get('input[name="password"]').type(adminData.password);

      cy.get('button[type="submit"]').click();

      cy.url().should("include", "/admin_login");

      cy.get('.doacao').click();
      


    
  });

  it('Doacao test - Caso desfavorável (campo obrigatório não preenchido)', () => {
    cy.contains('Doação e Coleta de Materiais').click();
    cy.get('.button').should('contain', 'Desejo Doar').click();
    cy.get('#nome_doador').type('Rafael Serpa');
    cy.get('#contato').type('(81) 99999-4215');
    cy.get('#data').type('2024-12-01'); 
    cy.get('#hora_inicio').type('09:00');
    cy.get('#hora_fim').type('12:00');
    cy.get('button[type="submit"]').click();
    
    
  });
});
