# Generated by Django 3.1.1 on 2020-09-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200911_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
