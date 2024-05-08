from django.db import models

# Create your models here.

class Atividade(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('C', 'Concluída'),
        ('A', 'Em andamento'),
    )

    nome = models.CharField('Nome da Tarefa', max_length=100)
    responsavel = models.CharField('Responsável pela Tarefa', max_length=100)
    prazo = models.CharField('Defina uma prazo de execução', max_length=100)
    observacoes = models.TextField('Descrição da atividade', blank=True)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return self.nome