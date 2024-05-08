from django.contrib import admin
from .models import Atividade

# Register your models here.

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'responsavel', 'status']

admin.site.register(Atividade, AtividadeAdmin)