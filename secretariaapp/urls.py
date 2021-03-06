from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views
from django.http import Http404


#nome do app
app_name='secretariaapp'

handler404 = 'secretariaapp.views.erro404'


#array
urlpatterns = [

    url(r'^$',index,name='index'),
    #url('igrejaelshaday.org', index,name='igrejaelshaday'),

    url(r'^login',auth_views.login,{'template_name': 'login.html'},name='login'),
    #url(r'^logout',auth_views.logout,{'template_name': 'index.html'},name='logout'),
    url(r'^logout',redirecionar,name='logout'),

    url(r'^recuperarsenha/(?P<recuperar>[0-9a-z]+)/$',recuperarsenha,name='recuperarsenha'),



    url(r'^sempermissao$',login_required(sempermissao),name='sempermissao'),
    url(r'^relatorios/(?P<imprimir>[relatorios,imprimir]+)/$',login_required(relatorios),name='relatorios'),
    url(r'^aniversariantes$',login_required(aniversariantes), name='aniversariantes'),
    url(r'^esqueceusenha$',esqueceuSenha,name='esqueceuSenha'),
    url(r'^suporte$',suporte,name='suporte'),


    url(r'^user/update/(?P<pk>[0-9]+)/$',login_required(UserUpdate.as_view()),name='userUpdate'),
    #url(r'^meu_user/update/(?P<pk>[0-9]+)/$',login_required(MeuUserUpdate.as_view()),name='meu_userUpdate'),
    url(r'^meu_user/update/$',login_required(meuUserUpdate),name='meu_perfil'),#nao generica
    url(r'^user/new/$',login_required(UserCreate.as_view()),name='userNew'),
    #url(r'^user/(?P<pk>[0-9]+)/$',login_required(userDetalhes),name='userDetalhes'),
    #url(r'^user/$',login_required(user),name='user'),
    url(r'^user/delete/(?P<pk>[0-9]+)/$',login_required(UserDelete.as_view()), name='userDelete'),
    #url(r'^user/meu_perfil/$',login_required(meu_perfil), name='meu_perfil'),

    #url(r'^perfil/alternativa/(?P<pk>[0-9]+)/$',login_required(perfilAlternativa),name='perfilAlternativa'),

    url(r'^meu_perfil/$',login_required(meu_perfilDetalhes),name='meu_perfilDetalhes'),
    #url(r'^meu_perfil/update/(?P<pk>[0-9]+)/$',login_required(MeuPerfilUpdate.as_view()),name='meu_perfilUpdate'),
    url(r'^meu_perfil/update/$',login_required(meuPerfilUpdate),name='meu_perfilUpdate'),

    url(r'^perfil/update/(?P<pk>[0-9]+)/$',login_required(PerfilUpdate.as_view()),name='perfilUpdate'),
    url(r'^perfil/(?P<pk>[0-9]+)/$',login_required(perfilDetalhes),name='perfilDetalhes'),
    url(r'^perfil/$',login_required(perfil),name='perfil'),


    url(r'^membros/new/$',login_required(MembroCreate.as_view()),name='membroNew'),
    url(r'^membros/(?P<pk>[0-9]+)/$',login_required(membroDetalhes),name='membroDetalhes'),
    #url(r'^membros/$',login_required(membro),name='membros'),
    url(r'^membros/$',login_required(membro),name='membros'),
    url(r'^membros/update/(?P<pk>[0-9]+)/$',login_required(MembroUpdate.as_view()),name='membroUpdate'),
    url(r'^membros/delete/(?P<pk>[0-9]+)/$',login_required(MembroDelete.as_view()), name='membroDelete'),

    url(r'^membro_grupo_pequeno_especifico/new/(?P<pk>[0-9]+)/$',login_required(membro_grupo_pequeno_especificoNew),name='membro_grupo_pequeno_especificoNew'),
    url(r'^membro_grupo_pequeno/new/$',login_required(membro_grupo_pequenoNew),name='membro_grupo_pequenoNew'),
    url(r'^membro_especifico_no_grupo_pequeno/new/(?P<pk>[0-9]+)/$',login_required(membro_especifico_no_grupo_pequenoNew),name='membro_especifico_no_grupo_pequenoNew'),


    url(r'^ministerios/new/$',login_required(MinisterioCreate.as_view()),name='ministerioNew'),
    url(r'^ministerios/(?P<pk>[0-9]+)/$',login_required(ministerioDetalhes),name='ministerioDetalhes'),
    url(r'^ministerios/$',login_required(ministerio),name='ministerios'),
    url(r'^ministerios/update/(?P<pk>[0-9]+)/$',login_required(MinisterioUpdate.as_view()),name='ministerioUpdate'),
    url(r'^ministerios/delete/(?P<pk>[0-9]+)/$',login_required(MinisterioDelete.as_view()), name='ministerioDelete'),


    url(r'^obreiro_ou_lider_delete/(?P<mt>[0-9]+)/(?P<mb>[0-9]+)/(?P<opc>[0-9]+)/$',login_required(obreiroOuLiderDelete),name='obreiroOuLiderDelete'),
    url(r'^obreiro_ou_lider_adicionar/(?P<mt>[0-9]+)/(?P<mb>[0-9]+)/(?P<opc>[0-9]+)/$',login_required(obreiroOuLiderAdicionar),name='obreiroOuLiderAdicionar'),

    url(r'^lider_gp_delete/(?P<gp>[0-9]+)/(?P<mb>[0-9]+)/$',login_required(liderGrupoPequenoDelete),name='liderGrupoPequenoDelete'),
    url(r'^lider_gp_adicionar/(?P<gp>[0-9]+)/(?P<mb>[0-9]+)/$',login_required(liderGrupoPequenoAdicionar),name='liderGrupoPequenoAdicionar'),



    url(r'^grupos_pequenos/new/$',login_required(Grupo_PequenoCreate.as_view()),name='grupo_pequenoNew'),
    url(r'^grupos_pequenos/(?P<pk>[0-9]+)/$',login_required(grupo_pequenoDetalhes),name='grupo_pequenoDetalhes'),
    url(r'^grupos_pequenos/$',login_required(grupo_pequeno),name='grupo_pequeno'),
    url(r'^grupos_pequenos/update/(?P<pk>[0-9]+)/$',login_required(Grupo_PequenoUpdate.as_view()),name='grupo_pequenoUpdate'),
    url(r'^grupos_pequenos/delete/(?P<pk>[0-9]+)/$',login_required(Grupo_PequenoDelete.as_view()), name='grupo_pequenoDelete'),

    url(r'^remover_membro_pg/(?P<pk_m>[0-9]+)/(?P<pk_pg>[0-9]+)/$',login_required(remover_membro_pg), name='remover_membro_pg'),


]
