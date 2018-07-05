from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register({Escolaridade, Estado_Civil, Grupo_Pequeno, Lider_Grupo_Pequeno, Membro, Origem, Sexo, Situacao, Uf, Ministerio, Lider_Ministerio, Obreiro_Ministerio, Perfil})#para o admin reconhecer suas classes
