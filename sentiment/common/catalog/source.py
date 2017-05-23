from ... import settings
import os


class Source:

    MOKORON = "mokoron"

    @staticmethod
    def get_list():
        return [
            Source.MOKORON,
        ]

    @staticmethod
    def get_path(source: str):
        paths = {}
        for source in Source.get_list():
            paths[source] = os.path.join(settings.BASE_DIR, 'database', 'raw', source.lower())
        return paths[source]
