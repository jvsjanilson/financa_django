from django.contrib import admin
from core.models import ContaReceber

@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ('documento', 'parcela', 'cliente', 'emissao', 'vencto', 'valor', 'data_pagto', 
    'valor_pago', 'situacao')
    
    fields = (('documento', 'parcela'), ('cliente','contacorrente'), ('emissao', 'vencto', 'valor'),
    ('data_pagto', 'valor_pago'), 'situacao')
