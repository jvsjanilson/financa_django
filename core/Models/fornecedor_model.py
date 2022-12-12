from django.db import models
from core.Models.estado_model import Estado
from core.Models.cidade_model import Cidade

class Fornecedor(models.Model):
    nome = models.CharField(max_length=60)
    nome_fantasia = models.CharField(max_length=60, blank=True, null=True)
    cpfcnpj = models.CharField(max_length=14, blank=True, null=True, verbose_name='CPF/CNPJ')
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