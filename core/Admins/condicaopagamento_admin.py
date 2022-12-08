from django.contrib import admin
from core.models import CondicaoPagamento

@admin.register(CondicaoPagamento)
class CondicaoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'formapagamento', 'tipo_intervalo', 'dia_fixo', 'ativo')
    fields = (('descricao', 'formapagamento'),  ('qtd_max_parcela', 'tipo_intervalo', 'intervalo'), 'dia_fixo', 'ativo')
    search_fields = ('descricao',)

    class Media:
        css = {
            'all': ('css/core.css',)
        }
