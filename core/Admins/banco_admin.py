from django.contrib import admin
from core.models import Banco

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    fields = (('codigo', 'descricao'), )
    search_fields = ('codigo', 'descricao')

    class Media:
        js = ("admin/js/jquery.init.js", "admin/js/vendor/jquery/jquery.js", "js/banco.js",)
