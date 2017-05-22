import configparser
import csv
from django.core.management.base import BaseCommand
import logging
import os
from ....common.catalog.sentiment_type import SentimentType
from ....common.catalog.source import Source


class Command(BaseCommand):
    help = 'Train the sentiment classifier'

    def add_arguments(self, parser):
        parser.add_argument(
            'type',
            type=str,
            help='Training data type',
            choices=SentimentType.get_list()
        )
        parser.add_argument(
            '--path',
            type=str,
            required=False,
            help="Path to csv file with training data"
        )
        parser.add_argument(
            '--source',
            type=str,
            required=False,
            help="Source with training data",
            choices=Source.get_list()
        )

    def handle(self, *args, **options):
        if options['source'] is None and options['path'] is None:
            message = 'Cant run training. Set --path or --source option.'
            logging.warning(message)
            self.stdout.write(self.style.WARNING(message))
            return

        if options['source'] is not None and options['path'] is not None:
            message = 'Cant run training. Set only one of --path or --source option.'
            logging.warning(message)
            self.stdout.write(self.style.WARNING(message))
            return

        path = options['path']
        if options['source'] is not None:
            path = os.path.join(Source.get_path(options['source']), options['type'] + '.csv')
        config_file = os.path.join(os.path.dirname(path), 'settings.ini')

        config = configparser.ConfigParser()
        config.read(config_file)
        column_index = int(config['csv']['IndexOfColumnWithData'])
        delimiter = config['csv']['Delimiter']
        encoding = config['csv']['Encoding']
        quote_char = config['csv']['QuoteChar']

        with open(path, newline='', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quote_char)
            for row in reader:
                print(row[column_index])
                return

        self.stdout.write('path: %s' % path)
        self.stdout.write(self.style.SUCCESS('Success'))