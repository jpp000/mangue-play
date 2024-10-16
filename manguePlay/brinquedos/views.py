from django.shortcuts import render, redirect
from .models import Brinquedo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def adicionar_brinquedo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        imagens = request.FILES.getlist('imagem')

        if not nome or not preco:
            messages.error(request, "Nome e preço são obrigatórios.")
            return render(request, 'adicionar_brinquedo.html')

        try:
            preco = float(preco)
            if preco <= 0:
                messages.error(request, "O preço deve ser um valor positivo.")
                return render(request, 'adicionar_brinquedo.html')
        except ValueError:
            messages.error(request, "Por favor, insira um valor numérico para o preço.")
            return render(request, 'adicionar_brinquedo.html')

        if not imagens:
            messages.error(request, "Por favor, carregue ao menos uma imagem.")
            return render(request, 'adicionar_brinquedo.html')

        for img in imagens:
            if not img.content_type.startswith('image/'):
                messages.error(request, "Os arquivos devem ser imagens.")
                return render(request, 'adicionar_brinquedo.html')

        brinquedo = Brinquedo.objects.create(nome=nome, preco=preco)
        for img in imagens:
            brinquedo.imagens.create(imagem=img)

        messages.success(request, "Brinquedo adicionado com sucesso.")
        return redirect('visualizar_brinquedos')
    
    return render(request, 'adicionar_brinquedo.html')

@login_required
def visualizar_brinquedos(req):
  brinquedos = Brinquedo.objects.all() 
  return render(req, 'visualizar_brinquedos.html', {
      'brinquedos': brinquedos
  })