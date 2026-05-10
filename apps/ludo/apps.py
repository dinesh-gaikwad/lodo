from django.apps import AppConfig

class LudoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.ludo"

    def ready(self):
        print("Ludo App Loaded")
