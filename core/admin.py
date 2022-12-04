from django.contrib import admin
from .models import ( Estado, Cidade, Cliente, FormaPagamento
, CondicaoPagamento, Banco, ContaCorrente)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    fields = (('uf', 'nome'), 'cod_ibge')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    fields = (('nome', 'estado'), 'cod_ibge')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpfcnpj', 'fone', 'celular', 'ativo')
    fields = (('nome', 'nome_fantasia'), ('cpfcnpj', 'insc_estadual', 'insc_municipal'), 
    ('logradouro', 'numero', 'cep'), ('complemento', 'bairro'), ('estado', 'cidade'),
    ('fone', 'celular', 'email'), 'ativo')


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


@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'banco', 'numero_agencia', 'numero_conta', 'data_abertura', 'data_fechamento', 'ativo')
    fields = (('descricao','banco'), ('numero_conta','numero_agencia'), ('data_abertura','data_fechamento'), 'ativo')