# Generated by Django 2.0.7 on 2019-05-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariaapp', '0010_membro_ministerios_que_lidera'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='grupos_pequenos_que_lidera',
            field=models.ManyToManyField(blank=True, related_name='grupo_pequeno_lider', to='secretariaapp.Grupo_Pequeno'),
        ),
    ]
