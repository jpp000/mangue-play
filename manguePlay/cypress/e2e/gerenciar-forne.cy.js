describe("Fornecedores - Admin", () => {
    const adminData = {
      username: "admin",
      email: "admin@example.com",
      password: "123",
      numeroTelefone: "123456789",
      isAdmin: true,
    };
  
    const fornecedor = {
      nome: "Fornecedor Reciclável",
      tipoMaterial: "Plástico",
      contato: "123456789",
      frequenciaEntrega: "Mensal",
      endereco: 'Endereco'
    };
  
    beforeEach(
      "Deve realizar o cadastro e login de um usuário administrador",
      () => {
        cy.exec('del /f db.sqlite3');
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
      }
    );
  
    it("Deve editar", () => {
      cy.visit("http://127.0.0.1:8000/fornecedor/listar/");
  
      cy.get('.add-button').click()
  
      cy.get('input[name="nome"]').type(fornecedor.nome);
      cy.get('input[name="contato_numero"]').type(fornecedor.contato);
      cy.get('select[name="frequencia_de_entrega"]').select(
        fornecedor.frequenciaEntrega
      );
      cy.get('input[name="endereco"]').type(fornecedor.endereco);
      cy.get('input[name="material"]').type(fornecedor.tipoMaterial);
  
      cy.get('button[type="submit"]').click();

    cy.visit("http://127.0.0.1:8000/fornecedor/listar/");

    cy.contains('📄').first().click();
    
    cy.get('input[name="nome"]').clear().type("Igor Couto");
    cy.get('input[name="material"]').clear().type("Tecido");

    cy.get('button').click()

    cy.visit("http://127.0.0.1:8000/fornecedor/listar/");
    });
  
    it("Deve excluir)", () =>{
      cy.visit("http://127.0.0.1:8000/fornecedor/listar/");
  
      cy.get('.add-button').click()
  
      cy.get('input[name="nome"]').type(fornecedor.nome);
      cy.get('input[name="contato_numero"]').type(fornecedor.contato);
      cy.get('select[name="frequencia_de_entrega"]').select(
        fornecedor.frequenciaEntrega
      );
      cy.get('input[name="endereco"]').type(fornecedor.endereco);
      cy.get('input[name="material"]').type(fornecedor.tipoMaterial);
  
      cy.get('button[type="submit"]').click();

    cy.visit("http://127.0.0.1:8000/fornecedor/listar/");

    cy.contains('🗑️').first().click();
    cy.contains('Excluir').click();
    });
    it("Deve dar erro ao não preencher campo de editar", () => {
      cy.visit("http://127.0.0.1:8000/fornecedor/listar/");
  
      cy.get('.add-button').click()
  
      cy.get('input[name="nome"]').type(fornecedor.nome);
      cy.get('input[name="contato_numero"]').type(fornecedor.contato);
      cy.get('select[name="frequencia_de_entrega"]').select(
        fornecedor.frequenciaEntrega
      );
      cy.get('input[name="endereco"]').type(fornecedor.endereco);
      cy.get('input[name="material"]').type(fornecedor.tipoMaterial);
  
      cy.get('button[type="submit"]').click();

    cy.visit("http://127.0.0.1:8000/fornecedor/listar/");

    cy.contains('📄').first().click();
    
    cy.get('input[name="nome"]').clear();
    cy.get('input[name="material"]').clear().type("Tecido");

    cy.contains('Salvar').click();
    });
  });
  