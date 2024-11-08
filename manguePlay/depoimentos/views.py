from django.shortcuts import render, redirect
from .models import Depoimento
from django import forms

class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['nome', 'texto']

def depoimentos_view(request):
    depoimentos = Depoimento.objects.all()

    if request.method == 'POST':
        form = DepoimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depoimentos')
    else:
        form = DepoimentoForm()

    context = {
        'form': form,
        'depoimentos': depoimentos
    }
    return render(request, 'depoimentos.html', context)
