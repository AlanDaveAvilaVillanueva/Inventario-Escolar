from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'ubicacion', 'fecha_ingreso')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre', 'ubicacion')
    ordering = ('nombre',)
