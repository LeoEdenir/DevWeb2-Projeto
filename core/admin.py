from django.contrib import admin
from . import models

admin.site.register(models.Categoria)


class ItensInline(admin.TabularInline):
    model = models.ExecucaoTarefa


@admin.register(models.Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    inlines = (ItensInline, )
