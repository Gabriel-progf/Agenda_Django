# Generated by Django 4.0.5 on 2022-06-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
