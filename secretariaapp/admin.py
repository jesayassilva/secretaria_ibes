from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register({Escolaridade, Estado_Civil, Grupo_Pequeno, Membro, Origem, Sexo, Situacao, Uf, Ministerio, Perfil, Trilha_Discipulado})#para o admin reconhecer suas classes
