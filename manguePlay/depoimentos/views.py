from django.shortcuts import render, redirect
from .models import Depoimento
from django import forms

# Formulário para Depoimento
class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['nome', 'email', 'telefone', 'anonimo', 'texto']

# View para exibir os depoimentos
def depoimentos_view(request):
    depoimentos = Depoimento.objects.all()
    context = {
        'depoimentos': depoimentos
    }
    return render(request, 'depoimentos.html', context)

# View para adicionar um novo depoimento
def adicionar_depoimento_view(request):
    if request.method == 'POST':
        form = DepoimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depoimentos')  # Redireciona para a página de depoimentos
    else:
        form = DepoimentoForm()

    context = {
        'form': form
    }
    return render(request, 'adicionar_depoimento.html', context)

# View para a administração dos depoimentos
def depoimentos_admin_view(request):
    depoimentos = Depoimento.objects.all()  # Recupera todos os depoimentos
    context = {
        'depoimentos': depoimentos
    }
    return render(request, 'depoimentos_admin.html', context)  # Renderiza o novo template
