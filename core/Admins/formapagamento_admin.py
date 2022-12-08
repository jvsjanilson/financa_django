from django.contrib import admin
from core.models import FormaPagamento

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'tipo')
    fields = (('codigo', 'descricao'), 'tipo')
    search_fields = ('codigo', 'descricao')
