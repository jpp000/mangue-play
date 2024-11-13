from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


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


def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'visualizar_forne.html', {'fornecedores': fornecedores})

def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        fornecedor.nome = request.POST['nome']
        fornecedor.contato_numero = request.POST['contato_numero']
        fornecedor.frequencia_de_entrega = request.POST['frequencia_de_entrega']
        fornecedor.endereco = request.POST['endereco']
        fornecedor.email = request.POST['email']
        fornecedor.save()

        messages.success(request, "Fornecedor atualizado com sucesso!")
        return redirect('listar_fornecedores')

    return render(request, 'editar_fornecedor.html', {'fornecedor': fornecedor})

def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        fornecedor.delete()
        messages.success(request, "Fornecedor excluído com sucesso!")
        return redirect('listar_fornecedores')

    return render(request, 'confirmar_exclusao.html', {'fornecedor': fornecedor})


