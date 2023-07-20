from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

# Create your models here.

User = get_user_model()


class ReportFragment(models.Model):
    cur_year = datetime.now().year
    YEAR_CHOICES = (
        (cur_year - 2, cur_year - 2),
        (cur_year - 1, cur_year - 1),
        (cur_year, cur_year),
        (cur_year + 1, cur_year + 1),
        (cur_year + 2, cur_year + 2),
    )

    verbose_name_plural = 'Фрагменты отчетов'
    verbose_name = 'Фрагмент отчета'

    report_name = models.CharField(
        'Название фрагмента',
        max_length=255
    )

    report_text = models.TextField(
        'Текст фрагмента'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    report_year = models.IntegerField(
        'Год отчета',
        choices=YEAR_CHOICES, default=cur_year
    )
    report_order = models.IntegerField(
        'Порядок сортировки (чем ниже, тем выше фрагмент в отчете)',
        default=500,
        validators=[
            MaxValueValidator(500),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(
        'Дата время публикации',
        auto_now_add=True
    )

    def __str__(self):
        return self.report_text

    class Meta:
        ordering = ('report_order',)
