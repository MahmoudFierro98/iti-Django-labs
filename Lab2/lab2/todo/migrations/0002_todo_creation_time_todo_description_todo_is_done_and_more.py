# Generated by Django 4.0.4 on 2022-06-06 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='Todo Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Todo Done'),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='Todo Priority'),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Todo Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Time'),
        ),
    ]
