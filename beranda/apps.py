from django.apps import AppConfig

class BerandaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beranda'

    def ready(self):
        import beranda.signals  # Gantilah 'beranda.signals' dengan modul yang sesuai jika diperlukan
