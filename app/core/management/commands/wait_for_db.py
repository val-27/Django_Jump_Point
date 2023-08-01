"""
Django command to wait for the database to be available!
"""

import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpErr


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for Database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpErr, OperationalError):
                self.stdout.write('Data Unavailable - Waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available.'))
