from django.apps import AppConfig

class RedirectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'redirect'

    def ready(self):
        import redirect.signals

# from __future__ import unicode_literals

# from django.apps import AppConfig


# class RedirectConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'app'

#     def ready(self):
#         import Redirect.signals
