from django.shortcuts import get_object_or_404, render, redirect
from .models import Brinquedo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
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
                raise ValueError("O preço deve ser um valor positivo.")
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
        return redirect('visualizar_brinquedos_admin')

    return render(request, 'adicionar_brinquedo.html')


@login_required
def editar_brinquedo(request):
    id = request.session.get('brinquedo_id')
    
    if request.method == 'POST':
        brinquedo = get_object_or_404(Brinquedo, id=id)

        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        novas_imagens = request.FILES.getlist('imagem')

        if not nome or not preco:
            messages.error(request, "Nome e preço são obrigatórios.")
            return render(request, 'editar_brinquedos.html', {'brinquedo': brinquedo})

        try:
            preco = float(preco)
            if preco <= 0:
                raise ValueError("O preço deve ser um valor positivo.")
        except ValueError:
            messages.error(request, "Por favor, insira um valor numérico para o preço.")
            return render(request, 'editar_brinquedos.html', {'brinquedo': brinquedo})

        brinquedo.nome = nome
        brinquedo.preco = preco
        brinquedo.save()

        for img in novas_imagens:
            if not img.content_type.startswith('image/'):
                messages.error(request, "Os arquivos devem ser imagens.")
                return render(request, 'editar_brinquedos.html', {'brinquedo': brinquedo})
            brinquedo.imagens.create(imagem=img)

        messages.success(request, "Brinquedo atualizado com sucesso.")
        return redirect('visualizar_brinquedos_admin')

    if not id:
        messages.error(request, "Nenhum brinquedo selecionado para edição.")
        return redirect('visualizar_brinquedos_admin')

    brinquedo = get_object_or_404(Brinquedo, id=id)
    return render(request, 'editar_brinquedos.html', {'brinquedo': brinquedo})

@login_required
def excluir_brinquedo(request, id):
    brinquedo = get_object_or_404(Brinquedo, id=id)
    brinquedo.delete()
    messages.success(request, "Brinquedo excluído com sucesso.")
    return redirect('visualizar_brinquedos_admin')

@login_required
def selecionar_brinquedo(request, id):
    request.session['brinquedo_id'] = id
    return redirect('editar_brinquedo')

@login_required
def visualizar_brinquedos(req):
    brinquedos = Brinquedo.objects.all()
    return render(req, 'visualizar_brinquedos.html', {'brinquedos': brinquedos})


@login_required
def visualizar_brinquedos_admin(req):
    brinquedos = Brinquedo.objects.all()
    return render(req, 'visualizar_brinquedos_admin.html', {'brinquedos': brinquedos})
