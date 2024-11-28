describe("Adicionar brinquedo - Admin", () => {
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

  it("Deve adicionar um brinquedo e verificar se ele aparece na lista", () => {
    cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");

    cy.get('input[name="nome"]').type(brinquedo.nome);
    cy.get('input[name="preco"]').type(brinquedo.preco);
    cy.get('input[type="file"]').selectFile(
      "cypress/fixtures/" + brinquedo.imagem
    );

    cy.get('button[type="submit"]').click();

    cy.visit("http://127.0.0.1:8000/brinquedos/visualizar_brinquedos/");

    cy.get(".card").contains(brinquedo.nome).should("be.visible");
    cy.get(".card").contains(`R$ ${brinquedo.preco}`).should("be.visible");
  });

  it("Deve exibir mensagens de erro ao não preencher campos obrigatórios", () => {
    cy.visit("http://127.0.0.1:8000/brinquedos/adicionar_brinquedo/");

    cy.get('button[type="submit"]').click();

    cy.get('input[name="nome"]:invalid')
      .should("have.length", 1)
      .and("have.prop", "validationMessage")
      .and("contain", "Preencha este campo.");
  });

});
