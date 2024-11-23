from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True, null=True)  # Email é opcional
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone é opcional
    anonimo = models.BooleanField(default=False)  # Checkbox para anonimato
    texto = models.TextField()

    def __str__(self):
        if self.anonimo:
            return f"Anônimo - {self.texto[:50]}"
        return f"{self.nome} - {self.texto[:50]}"
