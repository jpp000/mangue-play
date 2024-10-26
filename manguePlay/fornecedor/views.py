from django.shortcuts import render, redirect
from .models import Fornecedor

# View para adicionar fornecedor
def adicionar_fornecedor(request):
    
    if request.method == "POST":
        nome = request.POST['nome']
        contato_numero = request.POST['contato_numero']
        frequencia_de_entrega = request.POST['frequencia_de_entrega']
        endereco = request.POST['endereco']
        email = request.POST['email']

        # Cria um novo fornecedor
        fornecedor = Fornecedor(
            nome=nome,
            contato_numero=contato_numero,
            frequencia_de_entrega=frequencia_de_entrega,
            endereco=endereco,
            email=email
        )
        fornecedor.save()  # Salva o fornecedor no banco de dados

        return redirect('listar_fornecedores')  # Redireciona para a página de listagem após salvar

    return render(request, 'fornecedor.html')  # Renderiza o formulário para adicionar fornecedor

# View para listar fornecedores
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()  # Recupera todos os fornecedores do banco de dados
    return render(request, 'visualizar_forne.html', {'fornecedores': fornecedores})  # Renderiza a página de listagem
