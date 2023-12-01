from django.apps import AppConfig
from django.core.signals import setting_changed
from django.core.signals import request_finished
from django.dispatch import receiver

# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print("Request, finished")

def my_callback(sender, **kwargs) -> None:
    print("Settings changed!")


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) -> None:
        setting_changed.connect(my_callback)
