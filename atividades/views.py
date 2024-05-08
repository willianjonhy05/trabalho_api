from django.shortcuts import redirect
from .models import Atividade
from rest_framework import generics
from .serielizer import AtividadeSerialiezer, DetalharAtividade, AtividadeS
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
# from django.urls import reverse



@api_view(["GET"])
def getRoutes(request):
    routes = {
    "Criar Atividade": "http://127.0.0.1:8000/nova-atividade/",
    "Todas as Atividades": "http://127.0.0.1:8000/atividades/",
    "Atividade Pendentes": "http://127.0.0.1:8000/atividades-pendentes/",
    "Atividade em Andamento": "http://127.0.0.1:8000/atividades-em-andamento/",
    "Atividade Concluidas": "http://127.0.0.1:8000/atividades-concluidas/",
}
    return Response(routes)

# @api_view(["GET"])
# def getRoutes(request):
#     routes = {
#         "Criar Atividade": reverse('nova-atividade'),
#         "Todas as Atividades": reverse('atividades'),
#         "Atividade Pendentes": reverse('atividades-pendentes'),
#         "Atividade em Andamento": reverse('atividades-em-andamento'),
#         "Atividade Concluidas": reverse('atividades-concluidas'),
#     }
#     return Response(routes)

    
class CriarAtividade(generics.CreateAPIView):
    queryset = Atividade.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = AtividadeS

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)        
        return redirect('get-routes')


class ListaAtividades(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerialiezer

class ListaAtividadesPendentes(viewsets.ModelViewSet):
    queryset = Atividade.objects.filter(status='P')
    serializer_class = AtividadeSerialiezer

class ListaAtividadesEmAndamento(viewsets.ModelViewSet):
    queryset = Atividade.objects.filter(status='A')
    serializer_class = AtividadeSerialiezer

class ListaAtividadesConcluidas(viewsets.ModelViewSet):
    queryset = Atividade.objects.filter(status='C')
    serializer_class = AtividadeSerialiezer

class DetalharAtividade(generics.RetrieveAPIView):
    queryset = Atividade.objects.all()
    serializer_class = DetalharAtividade

class AtividadeAtualizar(generics.RetrieveUpdateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeS
    partial = True

class AtividadeDeletar(generics.DestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = DetalharAtividade

