from rest_framework import serializers
from .models import Estudiante, Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'valor']

class EstudianteSerializer(serializers.ModelSerializer):
    notas = NotaSerializer(many=True, read_only=True)

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'edad', 'correo', 'estado_activo', 'notas']
