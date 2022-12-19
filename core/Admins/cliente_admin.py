from django.contrib import admin
from core.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
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

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    @admin.action(description='Ativar cliente(s)')
    def ativar(self, request, queryset):
        count = queryset.update(ativo = True)

        if count == 1:
            message = '{} cliente foi ativado.'
        else:
            message = '{} clientes foram ativados.'
        
        self.message_user(request, message.format(count))    
    
    @admin.action(description='Desativar cliente(s)')
    def desativar(self, request, queryset):
        count = queryset.update(ativo = False)

        if count == 1:
            message = '{} cliente foi desativado.'
        else:
            message = '{} clientes foram desativados.'
        
        self.message_user(request, message.format(count))
