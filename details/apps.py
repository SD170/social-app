from django.apps import AppConfig


class DetailsConfig(AppConfig):
    name = 'details'
    def ready(self):
        import details.signals  