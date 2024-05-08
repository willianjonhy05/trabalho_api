from django.contrib import admin
from .models import Atividade

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'responsavel', 'status']

admin.site.register(Atividade, AtividadeAdmin)