from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    estado_activo = models.BooleanField(default=True)  # Controla si está visible o no

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, related_name='notas', on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.valor}"
