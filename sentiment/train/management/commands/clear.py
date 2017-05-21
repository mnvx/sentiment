from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Clear the sentiment classifier'

    def add_arguments(self, parser):
        parser.add_argument('--type', type=str, help='Clear training data type', required=False, choices=[
            'positive',
            'negative',
            'neutral',
        ])

    def handle(self, *args, **options):
        self.stdout.write('type: %s' % options['type'])
        self.stdout.write(self.style.SUCCESS('Successfully'))