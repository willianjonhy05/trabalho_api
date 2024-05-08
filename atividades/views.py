from django.shortcuts import render
from .models import Atividade
from rest_framework import generics
from .serielizer import AtividadeSerialiezer, DetalharAtividade, AtividadeS
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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

class AtividadeAtualizar(generics.UpdateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeS
    partial = True

class AtividadeDeletar(generics.DestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = DetalharAtividade

