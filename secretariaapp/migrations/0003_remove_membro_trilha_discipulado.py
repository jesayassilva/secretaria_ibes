# Generated by Django 2.0.7 on 2019-04-24 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretariaapp', '0002_auto_20190423_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='trilha_discipulado',
        ),
    ]
