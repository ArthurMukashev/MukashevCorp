from django.apps import AppConfig


class DiagramEditorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diagram_editor'
    verbose_name = 'Редактор диаграмм'
    icon = ''

    class Config:
        description = 'Диаграммы'
