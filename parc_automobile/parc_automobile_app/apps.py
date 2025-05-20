from django.apps import AppConfig


class ParcAutomobileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parc_automobile_app'

    def ready(self):
        import parc_automobile_app.signals
