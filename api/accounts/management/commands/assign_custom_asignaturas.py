from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.accounts.models import Asignatura

class Command(BaseCommand):
    help = 'Assign predefined Asignaturas to selected existing user'

    def handle(self, *args, **kwargs):
        asignaturas = [
            {'nombre': 'Programación Móvil', 'descripcion': 'Sección_003D'},
            {'nombre': 'Programación Base de Datos', 'descripcion': 'Sección_008D'},
            {'nombre': 'Arquitectura', 'descripcion': 'Sección_002D'},
            {'nombre': 'Portafolio', 'descripcion': 'Sección_005D'}
        ]

        try:
            user = User.objects.get(username='qwer')
            for asignatura_data in asignaturas:
                Asignatura.objects.get_or_create(usuario=user, **asignatura_data)
            self.stdout.write(self.style.SUCCESS('Successfully assigned Asignaturas to user qwer'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User qwer does not exist'))