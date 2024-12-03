from django.core.management.base import BaseCommand
from api.accounts.models import Asistencia

class Command(BaseCommand):
    help = 'Print all records from the Asistencia table'

    def handle(self, *args, **kwargs):
        asistencias = Asistencia.objects.all()
        for asistencia in asistencias:
            self.stdout.write(f'Usuario: {asistencia.usuario.user.username}, Asignatura: {asistencia.asignatura.nombre}, Fecha: {asistencia.fecha_asistencia}, Contador: {asistencia.contador}')