from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.accounts.models import PerfilUsuario, Asignatura, Asistencia

class Command(BaseCommand):
    help = 'Print all information about users, their subjects, and attendance'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f'Usuario: {user.username}, Email: {user.email}')
            try:
                perfil_usuario = PerfilUsuario.objects.get(user=user)
                asignaturas = perfil_usuario.asignaturas.all()
                for asignatura in asignaturas:
                    self.stdout.write(f'  Asignatura: {asignatura.nombre}, Descripción: {asignatura.descripcion}')
                    asistencias = Asistencia.objects.filter(usuario=perfil_usuario, asignatura=asignatura)
                    for asistencia in asistencias:
                        self.stdout.write(f'    Asistencia: {asistencia.fecha_asistencia}, Contador: {asistencia.contador}')
            except PerfilUsuario.DoesNotExist:
                self.stdout.write('  No tiene perfil de usuario.')