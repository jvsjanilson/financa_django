from django.db import models
from .choices import TypePayment, TypeIntervalo


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
    codigo = models.CharField(max_length=2, unique=True)
    descricao = models.CharField(max_length=60)
    tipo = models.SmallIntegerField(choices=TypePayment.choices, default=TypePayment.AVISTA)

    def __str__(self) -> str:
        return self.codigo


class CondicaoPagamento(models.Model):
    descricao = models.CharField(max_length=60)
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    qtd_max_parcela = models.SmallIntegerField(default=1)
    tipo_intervalo = models.CharField(max_length=2, choices=TypeIntervalo.choices, default=TypeIntervalo.DIARIO)
    intervalo = models.SmallIntegerField(default=0)
    dia_fixo = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.descricao

class Banco(models.Model):
    descricao = models.CharField(max_length=60)
    codigo = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return self.codigo


class ContaCorrente(models.Model):
    descricao = models.CharField(max_length=60)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    numero_conta = models.CharField(max_length=20)
    numero_agencia = models.CharField(max_length=10)
    data_abertura = models.DateField()
    data_fechamento = models.DateField(null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'Ag: {self.numero_agencia} - Conta: {self.numero_conta}'
