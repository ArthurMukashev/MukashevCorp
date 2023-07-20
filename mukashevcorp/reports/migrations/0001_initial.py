# Generated by Django 3.2 on 2023-07-20 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportFragment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.TextField(verbose_name='Текст фрагмента')),
                ('report_year', models.IntegerField(verbose_name='Год отчета')),
                ('report_order', models.IntegerField(default=500, verbose_name='Порядок сортировки (чем ниже, тем выше фрагмент в отчете)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
