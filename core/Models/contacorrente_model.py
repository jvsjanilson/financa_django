from django.db import models
from core.Models.banco_model import Banco


class ContaCorrente(models.Model):
    descricao = models.CharField(max_length=60)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_conta = models.CharField(max_length=20)
    numero_agencia = models.CharField(max_length=10)
    data_abertura = models.DateField()
    data_fechamento = models.DateField(null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'Ag: {self.numero_agencia} - Conta: {self.numero_conta}'
