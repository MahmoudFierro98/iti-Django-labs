# Generated by Django 4.0.4 on 2022-06-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='Todo Description'),
        ),
    ]