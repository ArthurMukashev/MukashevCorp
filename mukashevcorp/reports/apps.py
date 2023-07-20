from django.apps import AppConfig


class ReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reports'
    verbose_name = 'Отчеты'
    icon = 'reports.jpg'

    class Config:
        description = 'Система генерации отчетов'
