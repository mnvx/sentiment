from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Train the sentiment classifier'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Path to csv file with training data")
        parser.add_argument('type', type=str, help='Training data type', choices=[
            'positive',
            'negative',
            'neutral',
        ])

    def handle(self, *args, **options):
        self.stdout.write('path: %s' % options['path'])
        self.stdout.write('type: %s' % options['type'])
        self.stdout.write(self.style.SUCCESS('Successfully'))