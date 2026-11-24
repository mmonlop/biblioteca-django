from django.contrib import admin
from .models import Libro,Autor,Editorial,Prestamo,Usuario

# Register your models here.
#admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editorial)
#admin.site.register(Particicipacion)
admin.site.register(Prestamo)
admin.site.register(Usuario)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "isbn", "precio", "disponible", "editorial")
    list_filter = ("disponible","editorial")
    search_fields = ("titulo", "isbn", "autores__nombre")
    ordering = ("titulo",)
    list_per_page = 20
    filter_horizontal = ("autores",)