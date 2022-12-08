from django.contrib import admin
from core.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpfcnpj', 'fone', 'celular', 'ativo')
    fields = (('nome', 'nome_fantasia'), ('cpfcnpj', 'insc_estadual', 'insc_municipal'), 
    ('logradouro', 'numero', 'cep'), ('complemento', 'bairro'), ('estado', 'cidade'),
    ('fone', 'celular', 'email'), 'ativo')

    actions = ('desativar', 'ativar')

    class Media:
        js = ("admin/js/jquery.init.js", "admin/js/vendor/jquery/jquery.js", "js/cliente.js",)

    def desativar(self, request, queryset):
        count = queryset.update(ativo = 0)

        if count == 1:
            message = '{} cliente foi desativado.'
        else:
            message = '{} clientes foram desativados.'
        
        self.message_user(request, message.format(count))

    desativar.short_description = 'Desativar cliente(s)'

    def ativar(self, request, queryset):
        count = queryset.update(ativo = 1)

        if count == 1:
            message = '{} cliente foi ativado.'
        else:
            message = '{} clientes foram ativados.'
        
        self.message_user(request, message.format(count))

    ativar.short_description = 'Ativar cliente(s)'