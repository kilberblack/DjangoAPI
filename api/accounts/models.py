from django.db import models
from django.contrib.auth.models import User

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asignaturas')  # Relación con el usuario

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"

class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asistencias')  # Relación con el usuario
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField(auto_now_add=True)
    contador = models.PositiveIntegerField(default=0)  # Inicializamos en 0

    def __str__(self):
        return f"Asistencia {self.contador} para {self.asignatura.nombre} de {self.usuario.username} el {self.fecha}"