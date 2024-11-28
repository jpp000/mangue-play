describe("Gerenciar brinquedo - Admin", () => {
    const adminData = {
      username: "admin",
      email: "admin@example.com",
      password: "123",
      numeroTelefone: "123456789",
      isAdmin: true,
    };
  
    beforeEach("Deve realizar o cadastro e login de um usuário administrador", () => {
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

    it("Deve editar o brinquedo", () => {
      cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");
      cy.get('input[name="nome"]').type(brinquedo.nome);
    cy.get('input[name="preco"]').type(brinquedo.preco);
    cy.get('input[type="file"]').selectFile(
      "cypress/fixtures/" + brinquedo.imagem
    );
    cy.get('button[type="submit"]').click();
      cy.contains('Produtos').click();
      cy.contains('Editar').click();
      cy.get('#nome').clear().type("Carrinho");
      cy.contains('Salvar Alterações').click();
    });
    it("Deve excluir o brinquedo", () => {
        cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");
        cy.get('input[name="nome"]').type(brinquedo.nome);
      cy.get('input[name="preco"]').type(brinquedo.preco);
      cy.get('input[type="file"]').selectFile(
        "cypress/fixtures/" + brinquedo.imagem
      );
      cy.get('button[type="submit"]').click();
        cy.contains('Produtos').click();
        cy.contains('Excluir').click();
      });
      it("Deve dar erro ao tentar editar o brinquedo sem preencher todos os campos", () => {
        cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");
        cy.get('input[name="nome"]').type(brinquedo.nome);
      cy.get('input[name="preco"]').type(brinquedo.preco);
      cy.get('input[type="file"]').selectFile(
        "cypress/fixtures/" + brinquedo.imagem
      );
      cy.get('button[type="submit"]').click();
        cy.contains('Produtos').click();
        cy.contains('Editar').click();
        cy.get('#nome').clear();
        cy.contains('Salvar Alterações').click();
      });
  
  });
  