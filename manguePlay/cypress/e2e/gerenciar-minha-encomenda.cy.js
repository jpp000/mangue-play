

describe('Encomendar Brinquedo', () => {
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
    });
    
    const brinquedo = {
        nome: "lil messi",
        preco: "300",
        imagem: "messi.png",
      };
    it('Deve editar a encomenda', () => {
        cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");
        cy.get('input[name="nome"]').type(brinquedo.nome);
        cy.get('input[name="preco"]').type(brinquedo.preco);
        cy.get('input[type="file"]').selectFile(
          "cypress/fixtures/" + brinquedo.imagem);
        cy.get('button[type="submit"]').click();
        
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
      cy.contains('Produtos').click();
      cy.get('.edit-button').click();
      cy.get('#quantidade').type("12");
      cy.contains('Enviar Encomenda').click();
      cy.contains('Minhas encomendas').click();
      cy.contains('Editar').click();
      cy.get('#quantidade').clear().type("20");
      cy.contains('Salvar Alterações').click();
    });

    it('Deve dar erro ao tentar editar a encomenda sem preencher todos os campos', () => {
        cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");
        cy.get('input[name="nome"]').type(brinquedo.nome);
        cy.get('input[name="preco"]').type(brinquedo.preco);
        cy.get('input[type="file"]').selectFile(
          "cypress/fixtures/" + brinquedo.imagem);
        cy.get('button[type="submit"]').click();
        
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
      cy.contains('Produtos').click();
      cy.get('.edit-button').click();
      cy.get('#quantidade').type("12");
      cy.contains('Enviar Encomenda').click();
      cy.contains('Minhas encomendas').click();
      cy.contains('Editar').click();
      cy.get('#quantidade').clear();
      cy.contains('Salvar Alterações').click();
    });    
});
  