from django.core.management.base import BaseCommand

from franchises.models import  Franchise


class Command(BaseCommand):
    def handle(self, *args, **options):
        Franchise.initial_franchise()
