from django.contrib import admin
from .models import ReformaItem


@admin.register(ReformaItem)
class Reformas(admin.ModelAdmin):
    list_display = (
        'nome',
        'categoria',
        'custo_estimado',
        'custo_real',
        'status',
        'prioridade',
        'data_estimavel'
    )
