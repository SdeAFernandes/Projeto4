from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import Filmes, Generos


@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]


@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ["titulo", "generos", "ano_lancamento", "duracao"]
    search_fields = ["titulo", "descricao", "generos__nome"]
    list_filter = ["generos", "ano_lancamento"]

admin.site.register(Token)
