from django.apps import AppConfig


class DigitaltwinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digitaltwin'
    
    def ready(self):
        import digitaltwin.signals