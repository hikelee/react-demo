from django.apps import AppConfig
from django.db.models.signals import post_migrate

from snippets.management import init_models
class SnippetsConfig(AppConfig):
    name = 'snippets'

    def ready(self):
        post_migrate.connect(init_models)
         