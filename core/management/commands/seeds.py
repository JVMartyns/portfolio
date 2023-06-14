from django.core.management.base import BaseCommand

from core import seeds


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_LABEL('Seeding...'))

        for module in seeds.SEEDS:
            module.execute_seeds()

        self.stdout.write(
            self.style.SUCCESS(
                'Seed data created successfully.'
            )
        )
