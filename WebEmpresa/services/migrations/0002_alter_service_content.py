# Generated by Django 5.2.1 on 2025-05-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Contenido'),
        ),
    ]
