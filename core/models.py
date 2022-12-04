from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=120)
    uf = models.CharField(max_length=2)
    cod_ibge = models.IntegerField()

    def __str__(self) -> str:
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=120)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cod_ibge = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

