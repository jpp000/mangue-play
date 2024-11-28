from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doacao
from django.http import HttpResponse

# Exibe o formulário de doação
@login_required
def local_doacao(request):
    return render(request, 'local.html')
@login_required
def infolocal(request):  # Nome corrigido para "infolocal"
    return render(request, 'infolocal.html')

# Adiciona uma nova doação
@login_required
def adicionar_doacao(request):
    if request.method == 'POST':
        nome_doador = request.POST.get('nome_doador')
        contato = request.POST.get('contato')
        local = request.POST.get('local')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')
        observacoes = request.POST.get('observacoes')

        doacao = Doacao(
            nome_doador=nome_doador,
            contato=contato,
            local=local,
            data=data,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim,
            observacoes=observacoes
        )
        doacao.save()
        messages.success(request, 'Doação registrada com sucesso!')
        return redirect('user_dashboard')  # Redireciona para a página de visualização

    return render(request, 'local.html')

# Visualiza todas as doações
@login_required
def visualizar_local(request):
    doacoes = Doacao.objects.all()
    return render(request, 'visualizar_local.html', {'doacoes': doacoes})

# Edita uma doação existente
@login_required
def editar_doacao(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)

    if request.method == 'POST':
        doacao.nome_doador = request.POST.get('nome_doador')
        doacao.contato = request.POST.get('contato')
        doacao.local = request.POST.get('local')
        doacao.data = request.POST.get('data')
        doacao.hora_inicio = request.POST.get('hora_inicio')
        doacao.hora_fim = request.POST.get('hora_fim')
        doacao.observacoes = request.POST.get('observacoes')
        doacao.save()
        messages.success(request, 'Doação editada com sucesso!')
        return redirect('visualizar_local')

    return render(request, 'editar_local.html', {'doacao': doacao})

# Deleta uma doação
@login_required
def deletar_doacao(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    doacao.delete()
    messages.success(request, 'Doação deletada com sucesso!')
    return redirect('visualizar_local')
