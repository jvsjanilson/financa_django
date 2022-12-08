from django.db import models
from core.validators import number_only


class Banco(models.Model):
    descricao = models.CharField(max_length=60)
    codigo = models.CharField(max_length=3, unique=True, validators=[number_only])
    
    def __str__(self) -> str:
        return self.codigo