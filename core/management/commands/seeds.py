from django.core.management.base import BaseCommand

from core import seeds


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_LABEL('Seeding started...'))

        for module in seeds.SEEDS:
            try:
                self.stdout.write(
                    self.style.MIGRATE_LABEL(f'Seeding {module.__name__}...'),
                    ending=' '
                )
                module.execute_seeds()
                self.stdout.write(self.style.SUCCESS('OK'))
            except Exception:
                self.stderr.write(self.style.ERROR('ERROR'))
                raise

        self.stdout.write(
            self.style.SUCCESS(
                'Seed data created successfully.'
            )
        )
