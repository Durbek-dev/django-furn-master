# Generated by Django 4.0.6 on 2022-07-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0006_arrival_arrivals_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='arrivals_title',
            field=models.CharField(max_length=100),
        ),
    ]
