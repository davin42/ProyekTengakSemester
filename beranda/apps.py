from django.apps import AppConfig

class BerandaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beranda'

    def ready(self):
        import beranda.signals  # Impor file 'signals.py' atau yang sesuai dari modul 'beranda'
