from django.contrib import admin
from core.models import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    fields = (('nome', 'estado'), 'cod_ibge', 'capital')
    