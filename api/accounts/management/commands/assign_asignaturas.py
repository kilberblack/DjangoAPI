from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.accounts.models import Asignatura

class Command(BaseCommand):
    help = 'Assign predefined Asignaturas to all existing users'

    def handle(self, *args, **kwargs):
        asignaturas = [
            {'nombre': 'Programación Móvil', 'descripcion': 'Sección 003_D'},
            {'nombre': 'Programación Base de Datos', 'descripcion': 'sección_008A'},
            {'nombre': 'Arquitectura', 'descripcion': 'Sección_002C'},
            {'nombre': 'Portafolio', 'descripcion': 'Sección_005B'}
        ]

        users = User.objects.all()
        for user in users:
            for asignatura_data in asignaturas:
                Asignatura.objects.get_or_create(usuario=user, **asignatura_data)

        self.stdout.write(self.style.SUCCESS('Successfully assigned Asignaturas to all users'))