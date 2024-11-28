from django.db import models
from django.contrib.auth.models import User
from brinquedos.models import Brinquedo  

class Encomenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    brinquedo = models.ForeignKey(Brinquedo, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_encomenda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Encomenda de {self.quantidade} {self.brinquedo.nome} por {self.usuario.username}"
