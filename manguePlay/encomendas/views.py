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

        Encomenda.objects.create(usuario=request.user, brinquedo=brinquedo, quantidade=quantidade)
        messages.success(request, "Encomenda feita com sucesso.")
        return redirect('visualizar_encomendas')  # Supondo que você tenha essa view

    brinquedos = Brinquedo.objects.all()
    return render(request, 'adicionar_encomenda.html', {'brinquedos': brinquedos})

@login_required
def visualizar_encomendas(request):
    encomendas = Encomenda.objects.filter(usuario=request.user).order_by('-data_encomenda')
    return render(request, 'visualizar_encomendas.html', {'encomendas': encomendas})
