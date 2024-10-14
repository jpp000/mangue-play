from django.shortcuts import render, redirect
from .models import Doacao

def local_doacao(request):
    # Renderiza apenas o formulário
    return render(request, 'local.html')

def adicionar_doacao(request):
    if request.method == 'POST':
        nome_doador = request.POST.get('nome_doador')
        contato = request.POST.get('contato')
        local = request.POST.get('local')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')
        observacoes = request.POST.get('observacoes')

        # Criar uma nova instância e salvar no banco de dados
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

        # Redirecionar para a página inicial ou de confirmação
        return redirect('user_dashboard')  # Altere 'home' para o nome da view que você deseja redirecionar após salvar

    return render(request, 'local.html')
