from django.db import models
from core.choices import TypePayment


class FormaPagamento(models.Model):
    codigo = models.CharField(max_length=2, unique=True)
    descricao = models.CharField(max_length=60)
    tipo = models.SmallIntegerField(choices=TypePayment.choices, default=TypePayment.AVISTA)

    def __str__(self) -> str:
        return self.codigo

