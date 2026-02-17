from django.contrib import admin

from cards.models import Filosofo, Exibicao

class ListaFilosofos(admin.ModelAdmin):
    list_display = ("id", "nome", "referencias", "publicado", )
    list_display_links = ("id", "nome", )
    search_fields = ("nome", "slug", )
    #list_filter = ("nome",)
    list_editable = ("publicado", )
    list_per_page = 20

class ListaExibicoes(admin.ModelAdmin):
    list_display = ("id","id_filosofo", "data_exibicao",)
    list_display_links = ('id', 'data_exibicao',)
    list_per_page = 20
    ordering = ('-data_exibicao', )
# Register your models here.
admin.site.register(Filosofo, ListaFilosofos)
admin.site.register(Exibicao, ListaExibicoes)