from django.apps import AppConfig


class JabMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JAB_Main'
    
    def ready(self):
        import JAB_Main.signals