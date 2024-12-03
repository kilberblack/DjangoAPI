from django.db import models
from django.contrib.auth.models import User

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    asignaturas = models.ManyToManyField(Asignatura, through='Asistencia')

    def __str__(self):
        return self.user.username

class Asistencia(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField(auto_now_add=True)
    contador = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.user.username} - {self.asignatura.nombre}'