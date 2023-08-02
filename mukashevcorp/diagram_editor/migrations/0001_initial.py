# Generated by Django 3.2 on 2023-08-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc_short', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Схема',
                'verbose_name_plural': 'Схемы',
            },
        ),
        migrations.CreateModel(
            name='AccessMatrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagram_editor.informationschema')),
            ],
            options={
                'verbose_name': 'Матрица доступа',
                'verbose_name_plural': 'Матрицы доступа',
            },
        ),
    ]
