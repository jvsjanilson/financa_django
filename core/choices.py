from django.db import models
from django.utils.translation import gettext_lazy as _

class TypePayment(models.IntegerChoices):
    AVISTA = 1, _('A Vista')
    APRAZO = 2, _('A Prazo')


class TypeIntervalo(models.TextChoices):
    DIARIO = 'D', _('Diário')
    MENSAL = 'M', _('Mensal')
    ANUAL = 'A', _('Anual')

class TypeSituacao(models.TextChoices):
    ABERTO = 'A', _('Aberto')
    PAGO = 'P', _('Pago')
