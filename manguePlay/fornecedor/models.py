from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato_numero = models.CharField(max_length=20)  # Ex: Número de telefone
    frequencia_de_entrega = models.CharField(max_length=50)  # Ex: Semanal, Mensal
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
