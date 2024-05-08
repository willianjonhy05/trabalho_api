from django.urls import path
from .views import *


urlpatterns = [
    path('', getRoutes, name='get-routes'),    
    path('nova-atividade/', CriarAtividade.as_view(), name='nova-atividade'),
    path('atividades/<int:pk>/', DetalharAtividade.as_view(), name='atividade-detalhe'),
    path('atividades/<int:pk>/atualizar/', AtividadeAtualizar.as_view(), name='atividade-atualizar'),
    path('atividades/<int:pk>/deletar/', AtividadeDeletar.as_view(), name='atividade-deletar'),
    path('atividades/', ListaAtividades.as_view({'get': 'list'}), name='atividades'),
    path('atividades-pendentes/', ListaAtividadesPendentes.as_view({'get': 'list'}), name='atividades-pendentes'),
    path('atividades-em-andamento/', ListaAtividadesEmAndamento.as_view({'get': 'list'}), name='atividades-em-andamento'),
    path('atividades-concluidas/', ListaAtividadesConcluidas.as_view({'get': 'list'}), name='atividades-concluidas'),

]
