from django.contrib import admin
from .models import Autor, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_play = ('id', 'titulo', 'autor', 'data_publicacao', 'numero_paginas')
    search_fields = ['titulo']
    list_filter = ['autor', 'data_publicacao']
    
    
