from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


# Create your models here.

class InformationSchema(models.Model):
    name = models.CharField('Название', max_length=255)
    desc_short = models.CharField('Краткое описание', max_length=255)
    description = models.TextField('Подробное описание')

    linked = models.ManyToManyField('self', verbose_name='Связана с:', blank=True)
    history = HistoricalRecords()
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    permitted_groups = models.ManyToManyField(Group, verbose_name='Доступна для:', blank=False)

    class Meta:
        verbose_name = 'Схема'
        verbose_name_plural = 'Схемы'

    def __str__(self):
        return self.name


class AccessMatrix(models.Model):
    schema = models.ForeignKey(InformationSchema, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Матрица доступа'
        verbose_name_plural = 'Матрицы доступа'
