# Generated by Django 2.0.7 on 2019-04-24 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariaapp', '0003_remove_membro_trilha_discipulado'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='trilha_discipulado',
            field=models.ManyToManyField(to='secretariaapp.Trilha_Discipulado'),
        ),
    ]
