from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('outra-lista/', Home.as_view(queryset=Atividade.objects.all(), serializer_class=AtividadeS), name='home'),
    path('nova-atividade/', CriarAtividade.as_view(), name='nova-atividade'),
    path('atividades/<int:pk>/', DetalharAtividade.as_view(), name='atividade-detalhe'),
    path('atividades/<int:pk>/atualizar/', AtividadeAtualizar.as_view(), name='atividade-atualizar'),
    path('atividades/<int:pk>/deletar/', AtividadeDeletar.as_view(), name='atividade-deletar'),
    path('atividades/', ListaAtividades.as_view({'get': 'list'}), name='atividades'),
    path('atividades-pendentes/', ListaAtividadesPendentes.as_view({'get': 'list'}), name='atividades-pendentes'),
    path('atividades-em-andamento/', ListaAtividadesEmAndamento.as_view({'get': 'list'}), name='atividades-em-andamento'),
    path('atividades-concluidas/', ListaAtividadesConcluidas.as_view({'get': 'list'}), name='atividades-concluidas'),

]
