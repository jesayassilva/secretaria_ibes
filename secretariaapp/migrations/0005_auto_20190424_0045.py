# Generated by Django 2.0.7 on 2019-04-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariaapp', '0004_membro_trilha_discipulado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='trilha_discipulado',
            field=models.ManyToManyField(blank=True, to='secretariaapp.Trilha_Discipulado'),
        ),
    ]
