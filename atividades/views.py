from django.shortcuts import render, redirect
from .models import Atividade
from rest_framework import generics
from .serielizer import AtividadeSerialiezer, DetalharAtividade, AtividadeS
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view



@api_view(["GET"])
def getRoutes(request):
    routes = {
    "Criar Atividade": "http://127.0.0.1:8000/nova-atividade/",
    "Listar Atividades": "http://127.0.0.1:8000/atividades/"
}
    return Response(routes)


class Home(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeS
    
    def list(self, request):        
        queryset = self.get_queryset()
        serializer = AtividadeS(queryset, many=True)
        return Response(serializer.data)
    
class CriarAtividade(generics.CreateAPIView):
    queryset = Atividade.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = AtividadeS

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)        
        return redirect('get-routes')

# class AtividadeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Atividade.objects.all()
#         serializer = AtividadeSerialiezer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = AtividadeS(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     def retrieve(self, request, pk=None):
#         queryset = Atividade.objects.all()
#         atividade = get_object_or_404(queryset, pk=pk)
#         serializer = AtividadeS(atividade)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         atividade = Atividade.objects.get(pk=pk)
#         serializer = AtividadeS(atividade, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def destroy(self, request, pk=None):
#         atividade = Atividade.objects.get(pk=pk)
#         atividade.delete()
#         return Response(status=204)


class ListaAtividades(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
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

