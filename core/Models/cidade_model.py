from django.db import models
from core.Models.estado_model import Estado

class Cidade(models.Model):
    nome = models.CharField(max_length=120)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    capital = models.BooleanField(default=False)
    cod_ibge = models.IntegerField()

    def __str__(self) -> str:
        return self.nome