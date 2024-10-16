from django.db import models

# Create your models here.
from django.db import models

class Doacao(models.Model):
    nome_doador = models.CharField(max_length=100)
    contato = models.CharField(max_length=15)
    local = models.CharField(max_length=100)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Doação de {self.nome_doador} em {self.local} no dia {self.data}'
