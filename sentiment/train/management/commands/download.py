from django.core.management.base import BaseCommand
import os
import subprocess


class Command(BaseCommand):
    help = 'Download database for training'

    urls = {
        'mokoron': {
            'positive': 'https://www.dropbox.com/s/fnpq3z4bcnoktiv/positive.csv?dl=0',
            'negative': 'https://www.dropbox.com/s/r6u59ljhhjdg6j0/negative.csv?dl=0',
        }
    }

    def add_arguments(self, parser):
        parser.add_argument('source', type=str, help='Clear training data type', choices=[
            'mokoron',
        ])

    def handle(self, *args, **options):
        self.download(options['source'], 'positive')
        self.download(options['source'], 'negative')
        self.stdout.write(self.style.SUCCESS('Success'))

    def download(self, source: str, sentiment: str):
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
        path = os.path.join(path, 'database', 'raw', source)
        file = os.path.join(path, sentiment + '.csv')
        url = self.urls[source][sentiment];
        subprocess.call(['wget', url, '-O', file])
