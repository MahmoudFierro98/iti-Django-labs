# Generated by Django 4.0.4 on 2022-06-06 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='production_year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='update_time',
        ),
    ]