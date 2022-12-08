from django.db import models
from core.Models.formapagamento_model import FormaPagamento
from django.core.validators import MinValueValidator
from core.choices import TypeIntervalo


class CondicaoPagamento(models.Model):
    descricao = models.CharField(max_length=60, verbose_name='Descrição')
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, verbose_name='Formas de pagamento')
    qtd_max_parcela = models.SmallIntegerField(default=1, validators=[MinValueValidator(1, 'Valor minimo é 1.')])
    tipo_intervalo = models.CharField(max_length=2, choices=TypeIntervalo.choices, default=TypeIntervalo.DIARIO)
    intervalo = models.SmallIntegerField(default=0, validators=[MinValueValidator(0, 'Valor mínimo é 0.')])
    dia_fixo = models.BooleanField(default=False, verbose_name='Dia Fixo?')
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.descricao
