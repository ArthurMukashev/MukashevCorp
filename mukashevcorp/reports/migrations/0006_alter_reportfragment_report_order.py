# Generated by Django 3.2 on 2023-07-20 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_reportfragment_report_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfragment',
            name='report_order',
            field=models.IntegerField(default=500, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)], verbose_name='Порядок сортировки (чем ниже, тем выше фрагмент в отчете)'),
        ),
    ]
