from django.contrib import admin

from cards.models import Filosofo

class ListaFilosofos(admin.ModelAdmin):
    list_display = ("id", "nome", "referencias", "publicado")
    list_display_links = ("id", "nome",)
    search_fields = ("nome", "slug",)
    #list_filter = ("nome",)
    list_editable = ("publicado",)
    list_per_page = 20
# Register your models here.
admin.site.register(Filosofo, ListaFilosofos)