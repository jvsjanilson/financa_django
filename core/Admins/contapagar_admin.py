from django.contrib import admin
from core.models import ContaPagar

@admin.register(ContaPagar)
class ContaPagarAdmin(admin.ModelAdmin):
    list_display = ('documento', 'parcela', 'fornecedor', 'emissao', 'vencto', 'valor', 'data_pagto', 
    'valor_pago', 'situacao')
    
    fields = (('documento', 'parcela'), ('fornecedor','contacorrente'), ('emissao', 'vencto', 'valor'),
    ('data_pagto', 'valor_pago'), 'situacao')

    search_fields = ('documento', 'fornecedor__nome')
    
    class Media:
        css = {
            'all': ('css/core.css',)
        }