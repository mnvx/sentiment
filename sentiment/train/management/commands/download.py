from django.core.management.base import BaseCommand
import os
import subprocess
from ....settings import BASE_DIR
from ....common.catalog.sentiment_type import SentimentType


class Command(BaseCommand):
    help = 'Download database for training'

    urls = {
        'mokoron': {
            SentimentType.POSITIVE: 'https://www.dropbox.com/s/fnpq3z4bcnoktiv/positive.csv?dl=0',
            SentimentType.NEGATIVE: 'https://www.dropbox.com/s/r6u59ljhhjdg6j0/negative.csv?dl=0',
        }
    }

    def add_arguments(self, parser):
        parser.add_argument('source', type=str, help='Clear training data type', choices=[
            'mokoron',
        ])

    def handle(self, *args, **options):
        for sentiment_type in SentimentType.get_significant():
            self.download(options['source'], sentiment_type)

        self.stdout.write(self.style.SUCCESS('Success'))

    def download(self, source: str, sentiment: str):
        path = os.path.join(BASE_DIR, 'database', 'raw', source)
        file = os.path.join(path, sentiment + '.csv')
        url = self.urls[source][sentiment];
        subprocess.call(['wget', url, '-O', file])
