from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

atividade_list = AtividadeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

atividade_detail = AtividadeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',
    'delete': 'destroy'
})



urlpatterns = [
    path('', atividade_list, name='atividade-list'),
    path('atividades/<int:pk>/', atividade_detail, name='atividade-detail'),
    path('atividades/<int:pk>/', DetalharAtividade.as_view(), name='atividade-detalhe'),
#     path('atividades', ListaAtividades.as_view({'get': 'list'}), name='atividades'),
#     path('atividades/<int:pk>/', DetalharAtividade.as_view(), name='atividade-detalhe'),
#     path('atividades/<int:pk>/atualizar/', AtividadeAtualizar.as_view(), name='atividade-atualizar'),
#     path('atividades/<int:pk>/deletar/', AtividadeDeletar.as_view(), name='atividade-deletar'),
]

urlpatterns = format_suffix_patterns(urlpatterns)