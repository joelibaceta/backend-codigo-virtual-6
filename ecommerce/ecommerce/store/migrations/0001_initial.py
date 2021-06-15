# Generated by Django 3.2.4 on 2021-06-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('sku', models.CharField(max_length=15)),
            ],
        ),
    ]