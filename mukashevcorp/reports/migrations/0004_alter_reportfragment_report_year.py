# Generated by Django 3.2 on 2023-07-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20230720_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfragment',
            name='report_year',
            field=models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)], default=2023, verbose_name='Год отчета'),
        ),
    ]
