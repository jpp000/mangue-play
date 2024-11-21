from django.shortcuts import render, redirect, get_object_or_404
from .models import Encomenda
from brinquedos.models import Brinquedo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def adicionar_encomenda(request):
    if request.method == 'POST':
        brinquedo_id = request.POST.get('brinquedo')
        quantidade = request.POST.get('quantidade')

        brinquedo = get_object_or_404(Brinquedo, id=brinquedo_id)

        if not quantidade or int(quantidade) <= 0:
            messages.error(request, "Por favor, insira uma quantidade válida.")
            return redirect('adicionar_encomenda')

        encomenda = Encomenda(usuario=request.user, brinquedo=brinquedo, quantidade=quantidade)
        encomenda.save()
        print(encomenda)
        messages.success(request, "Encomenda feita com sucesso.")
        return redirect('user_dashboard')  

    brinquedos = Brinquedo.objects.all()
    return render(request, 'adicionar_encomenda.html', {'brinquedos': brinquedos})

@login_required
def visualizar_encomendas(request):
    encomendas = Encomenda.objects.filter(usuario=request.user).order_by('-data_encomenda')
    return render(request, 'visualizar_encomendas.html', {'encomendas': encomendas})

@login_required
def excluir_encomenda(request, encomenda_id):
    if request.method == 'POST':
        encomenda = get_object_or_404(Encomenda, id=encomenda_id, usuario=request.user)
        encomenda.delete()
        messages.success(request, "Encomenda excluída com sucesso.")
        return redirect('visualizar_encomendas')
    else:
        messages.error(request, "Requisição inválida.")
        return redirect('visualizar_encomendas')

@login_required
def editar_encomenda(request, id):
    encomenda = get_object_or_404(Encomenda, id=id, usuario=request.user)  # Certifica-se que a encomenda pertence ao usuário
    brinquedos = Brinquedo.objects.all()  # Obtém todos os brinquedos

    if request.method == 'POST':
        # Atualiza a encomenda com os novos dados
        encomenda.brinquedo_id = request.POST['brinquedo']  # ID do brinquedo selecionado
        encomenda.quantidade = request.POST['quantidade']  # Nova quantidade
        encomenda.save()
        messages.success(request, "Encomenda atualizada com sucesso.")
        return redirect('visualizar_encomendas')  # Redireciona para a página de visualização

    return render(request, 'editar_encomenda.html', {'encomenda': encomenda, 'brinquedos': brinquedos})


def listar_encomendas(req):
    encomendas = Encomenda.objects.all()
    return render(req, 'listar_encomendas.html', {'encomendas': encomendas})