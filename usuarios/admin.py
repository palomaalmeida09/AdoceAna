from django.contrib import admin

from usuarios.models import Usuario,Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "valor", "qtd"]

admin.site.register(Produto, ProdutoAdmin)