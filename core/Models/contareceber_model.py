from django.db import models
from core.Models.cliente_model import Cliente
from core.Models.contacorrente_model import ContaCorrente
from core.choices import TypeSituacao
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator


class ContaReceber(models.Model):
    documento = models.CharField(max_length=20, validators=[MinLengthValidator(limit_value=2)])
    parcela = models.IntegerField(default=1, validators=[MaxValueValidator(limit_value=360), MinValueValidator(limit_value=1)])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contacorrente = models.ForeignKey(ContaCorrente, on_delete=models.CASCADE)
    emissao = models.DateField()
    vencto = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0, validators=[MinValueValidator(limit_value=0)])
    data_pagto = models.DateField(null=True, blank=True)
    valor_pago = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, validators=[MinValueValidator(limit_value=0)])
    situacao = models.CharField(max_length=1, choices=TypeSituacao.choices, default=TypeSituacao.ABERTO)

    class Meta:
        verbose_name = 'Conta a receber'
        verbose_name_plural = 'Contas a receber'

    def __str__(self) -> str:
        return self.documento
