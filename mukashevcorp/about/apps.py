from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
    verbose_name = 'Об авторе'
    icon = 'about.jpg'

    class Config:
        description = 'Здесь вы можете увидеть информацию об авторе'
