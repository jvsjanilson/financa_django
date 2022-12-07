from django.contrib import admin
from .models import ( Estado, Cidade, Cliente, FormaPagamento
, CondicaoPagamento, Banco, ContaCorrente, ContaReceber)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    fields = (('uf', 'nome'), 'cod_ibge')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    fields = (('nome', 'estado'), 'cod_ibge', 'capital')
    
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpfcnpj', 'fone', 'celular', 'ativo')
    fields = (('nome', 'nome_fantasia'), ('cpfcnpj', 'insc_estadual', 'insc_municipal'), 
    ('logradouro', 'numero', 'cep'), ('complemento', 'bairro'), ('estado', 'cidade'),
    ('fone', 'celular', 'email'), 'ativo')

    class Media:
        js = ("admin/js/jquery.init.js", "admin/js/vendor/jquery/jquery.js", "js/cliente.js",)


@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'tipo')
    fields = (('codigo', 'descricao'), 'tipo')
    

@admin.register(CondicaoPagamento)
class CondicaoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'formapagamento', 'tipo_intervalo', 'dia_fixo', 'ativo')
    fields = (('descricao', 'formapagamento'),  ('qtd_max_parcela', 'tipo_intervalo','intervalo'), 'dia_fixo', 'ativo')


@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    fields = ('codigo', 'descricao')

    class Media:
        js = ("admin/js/jquery.init.js", "admin/js/vendor/jquery/jquery.js", "js/banco.js",)

@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'banco', 'numero_agencia', 'numero_conta', 'data_abertura', 'data_fechamento', 'saldo', 'ativo')
    fields = (('descricao','banco'), ('numero_conta','numero_agencia'), ('data_abertura','data_fechamento'), 'saldo', 'ativo')

@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ('documento', 'parcela', 'emissao', 'vencto', 'valor', 'data_pagto', 'valor_pago', 'situacao')
    
    fields = (('documento', 'parcela'), ('cliente','contacorrente'), ('emissao', 'vencto', 'valor'),
    ('data_pagto', 'valor_pago'), 'situacao')