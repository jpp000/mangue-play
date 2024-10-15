from django.db import models

# Create your models here.
from django.db import models

class Doacao(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=15, decimal_places=10)
    imagem = models.ImageField(upload_to='imagens/')
    
    def __str__(self):
        return f'Doação de {self.nome_doador} em {self.local} no dia {self.data}'
