from django.contrib import admin
from core.models import Estado


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    fields = (('uf', 'nome'), 'cod_ibge')
    