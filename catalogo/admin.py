from django.contrib import admin
from django.utils.html import mark_safe 
from .models import Novela

class NovelaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'genero_corto', 'ver_imagen')
    
    search_fields = ('titulo', 'genero')
    
    list_filter = ('tipo',)
    
    list_per_page = 10

    def ver_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="40" height="60" style="border-radius: 5px; border: 1px solid #ccc;">')
        return "Sin imagen"
    ver_imagen.short_description = 'Portada'

    def genero_corto(self, obj):
        return obj.genero[:30] + '...' if len(obj.genero) > 30 else obj.genero
    genero_corto.short_description = 'Géneros'


admin.site.register(Novela, NovelaAdmin)