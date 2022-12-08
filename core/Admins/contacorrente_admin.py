from django.contrib import admin
from core.models import ContaCorrente

@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'banco', 'numero_agencia', 'numero_conta', 'data_abertura', 'data_fechamento', 'saldo', 'ativo')
    fields = (('descricao','banco'), ('numero_conta','numero_agencia'), ('data_abertura','data_fechamento'), 'saldo', 'ativo')
    search_fields = ('descricao', 'numero_agencia', 'numero_conta')
    
    class Media:
        css = {
            'all': ('css/core.css',)
        }