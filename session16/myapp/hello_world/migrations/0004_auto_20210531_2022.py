# Generated by Django 3.2.3 on 2021-06-01 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0003_gretting_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gretting',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='gretting',
            name='temp',
        ),
    ]
