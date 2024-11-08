from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.texto[:50]}"
