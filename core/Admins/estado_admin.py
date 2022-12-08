from django.contrib import admin
from core.models import Estado


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    fields = (('uf', 'nome'), 'cod_ibge')
    search_fields = ('nome', 'uf')
    
    class Media:
        css = {
            'all': ('css/core.css',)
        }
