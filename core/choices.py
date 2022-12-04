from django.db import models
from django.utils.translation import gettext_lazy as _

class TypePayment(models.IntegerChoices):
    AVISTA = 1, _('A Vista')
    APRAZO = 2, _('A Prazo')