from .models import Atividade
from rest_framework import serializers
from django.urls import reverse


class AtividadeS(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'

class AtividadeSerialiezer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    link = serializers.SerializerMethodField()

    class Meta:
        model = Atividade
        fields = ('id', 'nome', 'status', 'link')

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('atividade-detalhe', kwargs={'pk': obj.pk}))
        return None

class DetalharAtividade(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    link_atualizar = serializers.SerializerMethodField()
    link_deletar = serializers.SerializerMethodField()

    class Meta:
        model = Atividade
        fields = ('id', 'nome', 'responsavel', 'observacoes', 'prazo', 'status', 'link_atualizar', 'link_deletar')

    def get_link_atualizar(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('atividade-atualizar', kwargs={'pk': obj.pk}))
        return None
    
    def get_link_deletar(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('atividade-deletar', kwargs={'pk': obj.pk}))
        return None