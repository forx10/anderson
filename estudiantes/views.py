from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Estudiante, Nota
from .serializer import EstudianteSerializer, NotaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    @action(detail=True, methods=['post'])
    def agregar_nota(self, request, pk=None):
        estudiante = self.get_object()
        nota = request.data.get('valor')
        if nota:
            Nota.objects.create(estudiante=estudiante, valor=float(nota))
            return Response({'message': 'Nota agregada correctamente'})
        return Response({'error': 'Debe enviar una nota'}, status=400)

    @action(detail=True, methods=['get'])
    def estado_aprobado(self, request, pk=None):
        estudiante = self.get_object()
        notas = estudiante.notas.all()
        promedio = sum(n.valor for n in notas) / len(notas) if notas else 0
        aprobado = promedio >= 3.0
        return Response({'promedio': promedio, 'aprobado': aprobado})
