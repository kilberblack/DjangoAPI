from django.core.management.base import BaseCommand
from api.accounts.models import Asignatura

class Command(BaseCommand):
    help = 'Delete all records from the Asignatura table'

    def handle(self, *args, **kwargs):
        Asignatura.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all Asignaturas'))