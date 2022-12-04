from django.db import models
from .choices import TypePayment


class Estado(models.Model):
    nome = models.CharField(max_length=120)
    uf = models.CharField(max_length=2)
    cod_ibge = models.IntegerField()

    def __str__(self) -> str:
        return self.uf


class Cidade(models.Model):
    nome = models.CharField(max_length=120)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cod_ibge = models.IntegerField()

    def __str__(self) -> str:
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    nome_fantasia = models.CharField(max_length=60, blank=True, null=True)
    cpfcnpj = models.CharField(max_length=14, blank=True, null=True)
    insc_estadual = models.CharField(max_length=14, blank=True, null=True)
    insc_municipal = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    fone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome


class FormaPagamento(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=60)
    tipo = models.SmallIntegerField(choices=TypePayment.choices, default=TypePayment.AVISTA)

    def __str__(self) -> str:
        return self.codigo

