from ...settings import BASE_DIR
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
            paths[source] = os.path.join(BASE_DIR, 'database', 'raw', source.lower())
        return paths[source]
