# Generated by Django 4.0.4 on 2022-06-06 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_todo_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-id'], 'verbose_name': 'Todo', 'verbose_name_plural': 'Todos'},
        ),
    ]