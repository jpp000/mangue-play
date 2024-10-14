from django.shortcuts import render

# Create your views here.
def local_doacao(request):
    return render(request, 'local.html')