from django.db import models

class Brinquedo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Doação de {self.nome}'

class Imagem(models.Model):
    brinquedo = models.ForeignKey(Brinquedo, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='imagens/')
    
    def __str__(self):
        return f'Imagem de {self.brinquedo.nome}'
