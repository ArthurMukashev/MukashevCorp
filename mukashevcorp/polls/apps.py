from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    verbose_name = 'Голосование'
    icon = 'polls.jpg'

    class Config:
        description = 'Простой опросник по документации Django 3.2'
