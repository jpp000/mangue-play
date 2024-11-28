from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Fornecedor

# View para adicionar fornecedor
def adicionar_fornecedor(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        contato_numero = request.POST.get('contato_numero')
        frequencia_de_entrega = request.POST.get('frequencia_de_entrega')
        endereco = request.POST.get('endereco')
        material = request.POST.get('material')

        # Verificando se todos os campos obrigatórios estão preenchidos
        if not nome or not contato_numero or not frequencia_de_entrega or not endereco or not material:
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
            return render(request, 'fornecedor.html')

        # Salvando o fornecedor
        fornecedor = Fornecedor(
            nome=nome,
            contato_numero=contato_numero,
            frequencia_de_entrega=frequencia_de_entrega,
            endereco=endereco,
            material=material
        )
        fornecedor.save()

        messages.success(request, "Fornecedor adicionado com sucesso!")
        return redirect('listar_fornecedores')

    return render(request, 'fornecedor.html')


# View para listar fornecedores
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'visualizar_forne.html', {'fornecedores': fornecedores})


# View para editar fornecedor
def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        fornecedor.nome = request.POST.get('nome')
        fornecedor.contato_numero = request.POST.get('contato_numero')
        fornecedor.frequencia_de_entrega = request.POST.get('frequencia_de_entrega')
        fornecedor.endereco = request.POST.get('endereco')
        fornecedor.material = request.POST.get('material')

        # Validando se os campos obrigatórios foram preenchidos
        if not fornecedor.nome or not fornecedor.contato_numero or not fornecedor.frequencia_de_entrega or not fornecedor.endereco  or not fornecedor.material:
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
            return render(request, 'editar_fornecedor.html', {'fornecedor': fornecedor})

        fornecedor.save()

        messages.success(request, "Fornecedor atualizado com sucesso!")
        return redirect('listar_fornecedores')

    return render(request, 'editar_fornecedor.html', {'fornecedor': fornecedor})


# View para excluir fornecedor
def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        fornecedor.delete()
        messages.success(request, "Fornecedor excluído com sucesso!")
        return redirect('listar_fornecedores')

    return render(request, 'confirmar_exclusao.html', {'fornecedor': fornecedor})
