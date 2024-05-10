# Generated by Django 5.0.6 on 2024-05-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome da Tarefa'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Descrição da atividade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='prazo',
            field=models.CharField(max_length=100, verbose_name='Defina uma prazo de execução'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='responsavel',
            field=models.CharField(max_length=100, verbose_name='Responsável pela Tarefa'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('C', 'Concluída'), ('A', 'Em andamento')], default='P', max_length=1, verbose_name='Status'),
        ),
    ]
