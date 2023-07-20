from django.apps import AppConfig


class ZooConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zoo'
    verbose_name = 'Зоопарк'
    icon = 'zoo.jpg'

    class Config:
        description = 'Управление мини-зоопарком'
