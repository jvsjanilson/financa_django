from django.contrib import admin
from core.models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpfcnpj', 'fone', 'celular', 'ativo')
    fields = (('nome', 'nome_fantasia'), ('cpfcnpj', 'insc_estadual', 'insc_municipal'), 
    ('logradouro', 'numero', 'cep', 'complemento', 'bairro', 'estado'), 'cidade',
    ('fone', 'celular', 'email'), 'ativo')
    search_fields = ('nome', 'nome_fantasia', 'cpfcnpj', 'insc_estadual', 'fone', 'celular')
    list_filter = ('ativo',)

    actions = ('desativar', 'ativar')

    class Media:
        js = ("admin/js/jquery.init.js", "admin/js/vendor/jquery/jquery.js", "js/cidades_lookup.js",)
        css = {
            'all': ('css/core.css',)
        }

    def desativar(self, request, queryset):
        count = queryset.update(ativo = 0)

        if count == 1:
            message = '{} Fornecedor foi desativado.'
        else:
            message = '{} Fornecedores foram desativados.'
        
        self.message_user(request, message.format(count))

    desativar.short_description = 'Desativar Forncedor(es)'

    def ativar(self, request, queryset):
        count = queryset.update(ativo = 1)

        if count == 1:
            message = '{} Forncedor foi ativado.'
        else:
            message = '{} Fornecedores foram ativados.'
        
        self.message_user(request, message.format(count))

    ativar.short_description = 'Ativar Forncedor(es)'
    