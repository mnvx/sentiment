from django.core.management.base import BaseCommand
import urllib.request
import os
# import wget
# import dropbox


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

        self.stdout.write('source: %s' % options['source'])
        self.stdout.write(self.style.SUCCESS('Successfully'))

    def download(self, source: str, sentiment: str):
        path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
        path = os.path.join(path, 'database', 'raw', source)
        url = self.urls[source][sentiment];
        urllib.request.urlretrieve(url, os.path.join(path, sentiment + '.csv'))
        # wget.download(url, path)
        # dbx = dropbox.Dropbox
        # dbx.files_download_to_file(path, url)
