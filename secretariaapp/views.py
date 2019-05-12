from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm,UserChangeForm,PasswordResetForm
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *
#from .forms import *
import datetime
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth import authenticate
# Create your views here.
import copy

from django.http import *

from django.contrib.auth import logout

from django.core.mail import send_mail #Para mandar email
from random import randint


'''
    gerenciar_Membros = models.BooleanField(default = False)
    gerenciar_Grupos_Pequenos = models.BooleanField(default = False)
    gerenciar_Ministerios = models.BooleanField(default = False)
    gerenciar_Relatorios = models.BooleanField(default = False)
    gerenciar_Usuarios = models.BooleanField(default = False)

'''

def index(request):
    usuario = request.user
    try:
        perfil = Perfil.objects.get(user=usuario)
        if forcar_user_atualizar_perfil(request) :
            return redirect('/meu_perfil/update/')
    except Exception as e:
        userIsLogado = 'Não'
    return render(request,'index.html',{'usuario':usuario})

def redirecionar(request):
    request.session.items = []
    request.session.modified = True
    logout(request)
    return render(request,'redirect.html')

def relatorios(request, imprimir):
    if not request.user.perfil.gerenciar_Relatorios:
        return redirect('/sempermissao')
    if imprimir == 'imprimir':
        isImprimir = True
    elif imprimir == 'relatorios':
        isImprimir = False
    else:
        return redirect('/')


    membros_ativo = Membro.objects.filter(situacao__situacao = 'ATIVO' ).count()
    membros_disciplinado = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO' ).count()
    grupos_pequenos = Grupo_Pequeno.objects.all().count()
    ministerios = Ministerio.objects.all().count()



    trilha_discipulado = Trilha_Discipulado.objects.all()
    membro = Membro.objects.filter(situacao__situacao = 'ATIVO' )
    trilha = []
    for td in trilha_discipulado:
        cont = 0
        for mb in membro:
            for item in mb.trilha_discipulado.all():
                if item == td:
                    cont = cont +1
        try:
            porTrilha = 100/membros_ativo * cont
        except Exception as e:
            porTrilha = 0
        trilha.append({
        "nome": td.trilha_discipulado,
        "quantidade":cont,
        "porTrilha":porTrilha
        })






    membros_chegada_1mes = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=30)) ).count()
    membros_chegada_2mes = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=60)) ).count()
    membros_chegada_4mes = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=120)) ).count()
    membros_chegada_6mes = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=180)) ).count()
    membros_chegada_1ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=365)) ).count()
    membros_chegada_2ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=730)) ).count()
    membros_chegada_4ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=1460)) ).count()
    membros_chegada_8ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=2920)) ).count()
    membros_chegada_15ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=5475)) ).count()
    membros_chegada_30ano = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday__gt = (datetime.now() - timedelta(days=10950)) ).count()
    membros_chegada_nao_informada = Membro.objects.filter(situacao__situacao = 'ATIVO', data_chegada_na_elshaday = None ).count()

    membros_disciplinado_2mes = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=60)) ).count()
    membros_disciplinado_4mes = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=120)) ).count()
    membros_disciplinado_6mes = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=180)) ).count
    membros_disciplinado_1ano = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=365)) ).count()
    membros_disciplinado_2ano = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=730)) ).count()
    membros_disciplinado_4ano = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=1460)) ).count()
    membros_disciplinado_8ano = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao__gt = (datetime.now() - timedelta(days=2920)) ).count()
    membros_disciplinado_nao_informada = Membro.objects.filter(situacao__situacao = 'DISCIPLINADO', data_situacao = None ).count()

    membros_ativo_8idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__gt = (datetime.now() - timedelta(days=3287)) ).count()
    membros_ativo_14idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__gt = (datetime.now() - timedelta(days=5478)), data_nascimento__lte = (datetime.now() - timedelta(days=3287)) ).count()
    membros_ativo_30idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__gt = (datetime.now() - timedelta(days=11322)), data_nascimento__lte = (datetime.now() - timedelta(days=5478)) ).count()
    membros_ativo_50idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__gt = (datetime.now() - timedelta(days=18627)), data_nascimento__lte = (datetime.now() - timedelta(days=11322)) ).count()
    membros_ativo_75idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__gt = (datetime.now() - timedelta(days=27758)), data_nascimento__lte = (datetime.now() - timedelta(days=18627)) ).count()
    membros_ativo_110idade = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento__lte = (datetime.now() - timedelta(days=27758)) ).count()
    membros_ativo_idade_nao_informada = Membro.objects.filter(situacao__situacao = 'ATIVO', data_nascimento = None ).count()
    #, data_nascimento__lte = (datetime.now() - timedelta(days=2920))
    #membros_ativo_14idade = membros_ativo_14idade - membros_ativo_8idade


    membros_ativo_participacao_ministerio = 0
    membros_ativo_participacao_ministerio = membros_ativo - Membro.objects.filter(ministerios = None, situacao__situacao = 'ATIVO').count()
    '''
    for aux1 in Membro.objects.filter(situacao__situacao = 'ATIVO' ):
        for aux2 in Obreiro_Ministerio.objects.filter(obreiro__situacao__situacao = 'ATIVO' ):
            if aux1.pk == aux2.obreiro.pk :
                membros_ativo_participacao_ministerio = membros_ativo_participacao_ministerio + 1
                break
    '''

    membros_ativo_sem_participacao_ministerio = membros_ativo - membros_ativo_participacao_ministerio
    try:
        porcentagem_membros_ativo_participacao_ministerio = 100 / membros_ativo * membros_ativo_participacao_ministerio
    except Exception as e:
        porcentagem_membros_ativo_participacao_ministerio = 0

    '''
    membros_ativo_participacao_lideranca = 0

    for item in Membro.objects.filter(situacao__situacao = 'ATIVO' ):
        if item.ministerios_que_lidera != None:
            membros_ativo_participacao_lideranca = membros_ativo_participacao_lideranca + 1
            break
        if item.grupos_pequenos_que_lidera != None:
            membros_ativo_participacao_lideranca = membros_ativo_participacao_lideranca + 1
            break

    for aux1 in Membro.objects.filter(situacao__situacao = 'ATIVO' ):
        quebrar_laco = False
        for aux2 in Lider_Ministerio.objects.filter(nome_lider__situacao__situacao = 'ATIVO' ):
            if aux1.pk == aux2.nome_lider.pk :
                membros_ativo_participacao_lideranca = membros_ativo_participacao_lideranca + 1
                quebrar_laco = True
                break
        for aux3 in Lider_Grupo_Pequeno.objects.filter(lider__situacao__situacao = 'ATIVO' ):
            if quebrar_laco:
                break
            if aux1.pk == aux3.lider.pk :
                membros_ativo_participacao_lideranca = membros_ativo_participacao_lideranca + 1
                break

    try:
        porcentagem_membros_ativo_participacao_lideranca = 100 / membros_ativo * membros_ativo_participacao_lideranca
    except Exception as e:
        porcentagem_membros_ativo_participacao_lideranca = 0
    '''

    membros_ativo_participacao_gp = membros_ativo - Membro.objects.filter(grupo_pequeno = None, situacao__situacao = 'ATIVO').count()
    try:
        porcentagem_membros_ativo_participacao_gp = 100 / membros_ativo * membros_ativo_participacao_gp
    except Exception as e:
        porcentagem_membros_ativo_participacao_gp = 0


    dados = {
    'isImprimir' : isImprimir,
    'membros_ativo':membros_ativo,
    'membros_disciplinado':membros_disciplinado,
    'grupos_pequenos': grupos_pequenos,
    'ministerios': ministerios,
    'membros_chegada_1mes':membros_chegada_1mes,
    'membros_chegada_2mes':membros_chegada_2mes,
    'membros_chegada_4mes':membros_chegada_4mes,
    'membros_chegada_6mes':membros_chegada_6mes,
    'membros_chegada_1ano':membros_chegada_1ano,
    'membros_chegada_2ano':membros_chegada_2ano,
    'membros_chegada_4ano':membros_chegada_4ano,
    'membros_chegada_8ano':membros_chegada_8ano,
    'membros_chegada_15ano':membros_chegada_15ano,
    'membros_chegada_30ano':membros_chegada_30ano,
    'membros_chegada_nao_informada':membros_chegada_nao_informada,
    'membros_disciplinado_2mes':membros_disciplinado_2mes,
    'membros_disciplinado_4mes':membros_disciplinado_4mes,
    'membros_disciplinado_6mes':membros_disciplinado_6mes,
    'membros_disciplinado_1ano':membros_disciplinado_1ano,
    'membros_disciplinado_2ano':membros_disciplinado_2ano,
    'membros_disciplinado_4ano':membros_disciplinado_4ano,
    'membros_disciplinado_8ano':membros_disciplinado_8ano,
    'membros_disciplinado_nao_informada':membros_disciplinado_nao_informada,
    'membros_ativo_8idade':membros_ativo_8idade,
    'membros_ativo_14idade':membros_ativo_14idade,
    'membros_ativo_30idade':membros_ativo_30idade,
    'membros_ativo_50idade':membros_ativo_50idade,
    'membros_ativo_75idade':membros_ativo_75idade,
    'membros_ativo_110idade':membros_ativo_110idade,
    'membros_ativo_idade_nao_informada':membros_ativo_idade_nao_informada,
    'membros_ativo_participacao_ministerio':membros_ativo_participacao_ministerio,
    'membros_ativo_sem_participacao_ministerio': membros_ativo_sem_participacao_ministerio,
    'porcentagem_membros_ativo_participacao_ministerio' : porcentagem_membros_ativo_participacao_ministerio,
    #'membros_ativo_participacao_lideranca':membros_ativo_participacao_lideranca,
    #'porcentagem_membros_ativo_participacao_lideranca':porcentagem_membros_ativo_participacao_lideranca
    'membros_ativo_participacao_gp' : membros_ativo_participacao_gp,
    'porcentagem_membros_ativo_participacao_gp' : porcentagem_membros_ativo_participacao_gp,

    }


    return render(request,'relatorios.html',{'dados':dados,'trilha':trilha})


def aniversariantes(request):
    if not request.user.perfil.gerenciar_Membros:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')

    situacao_ativo = Situacao.objects.get(situacao = 'ATIVO')
    qtd = 0
    dia=1
    membros = None
    if  request.method == "POST":
        mes = request.POST.get("mes_aniversariantes")
        #consertar depois
        #membros = Membro.objects.filter(situacao = situacao_ativo, data_nascimento__month = mes).order_by('data_nascimento')
        #return render(request,'aniversariantes.html',{'membros':membros, 'qtd':qtd})
        membros = []
        while dia<=31:
            membrosN = Membro.objects.filter(situacao = situacao_ativo, data_nascimento__month = mes, data_nascimento__day = dia)
            for item in membrosN:
                membros.append({
                "pk": item.pk,
                "nome_completo":item.nome_completo,
                "situacao":item.situacao,
                "data_nascimento": item.data_nascimento,
                "sexo":item.sexo,
                "naturalidade":item.naturalidade,
                "telefone_celular": item.telefone_celular,
                "data_conversao":item.data_conversao,
                "grupo_pequeno":item.grupo_pequeno
                })
                qtd = qtd + 1
            dia = dia +1
        #Gambiara Editar depois pois se mudar nome de campo pode dar erro
    return render(request,'aniversariantes.html',{'membros':membros, 'qtd':qtd})



def sempermissao(request):
    #usuario = Aluno.objects.get(id=12)
    usuario = request.user
    #return HttpResponse(usuario)
    return render(request,'sempermissao.html',{'usuario':usuario})

def erro404(request):
    return render(request,'404.html')

def erro500(request):
    return render(request,'500.html')


def esqueceuSenha(request):
    if  request.method == "POST":
        email = request.POST.get("email")
        try:
            perfil = Perfil.objects.get(email = email)
            perfil = perfil
            a,b,c,d,e,f = randint(7679,839766548), randint(3629,83966548), randint(3679,83976548),randint(7674,839786548), randint(5643,83966548), randint(6769,8397652)
            #return HttpResponse(x)
            perfil.recuperar = 'ibes7kgjmspi'+str(a)+'ksh'+str(b)+'xi'+str(c)+'8fdgckm0'+str(d)+'15jesa'+str(e)+'vkel'+str(f)+'hji87g'
            perfil.data_recuperar = (datetime.now() + timedelta(seconds=7200))
            perfil.save()
            msg = 'Caro '+str(perfil.user.username)+ ' \n\nRecentemente, uma solicitação foi enviada para redefinir sua senha para nossa área de cliente. Se você não solicitou isso, ignore este e-mail. Ele irá expirar e se tornar inútil em 2 horas.  \n\nPara redefinir sua senha, visite o URL abaixo:  \nwww.elshaday.ml/recuperarsenha/'+str(perfil.recuperar)+ ' \n\nAo visitar o link acima, você terá a oportunidade de escolher uma nova senha. \n\nAtt \nJesaías Silva'
            send_mail(
            'Recuperar Login e Senha',#Titulo da msg
            msg,#Mensagem
            'jcps.suporte@gmail.com',
            [email],
            fail_silently=False,
            )
        except Exception as e:
            return HttpResponse("Email Inválido")
        return redirect('/login/')
    return render(request,'esqueceusenha.html')

def recuperarsenha(request,recuperar):
    if not(Perfil.objects.filter(recuperar = str(recuperar),data_recuperar__gt = datetime.now()  ) ):
        return HttpResponse("Sua Solicitação é Inválida")

    erro = ''
    if  request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if not (password1 == password2) :
            erro = erro + 'Suas senhas não são iguais. '
        numero = 0
        for caracter in password1:
            if caracter in '0123456789':
                numero = numero + 1
        if len(password1) <8 :
            erro = erro + 'Senha muito curta. '
        if len(password1) - numero < 1:
            erro = erro + 'Sua senha não pode ser apenas numerico. '
        #if password1 == username:
        #    erro = erro +'Sua senha não pode ser seu nome de Usuário. '
        if erro != '':
            return render(request,'recuperarsenha.html',{'erro':erro})

        try:
            perfil = Perfil.objects.get(email=email)
            user = User.objects.get(pk = perfil.user.pk)
            if str(user.perfil.recuperar) == str(recuperar):
                #if user.perfil.data_recuperar__gt = datetime.now():
                if User.objects.filter(pk=user.pk,perfil__data_recuperar__gt = datetime.now()):
                    user.set_password(password1)
                    user.save()
                    return redirect('/')
                else:
                    return HttpResponse("Sua Solicitação expirou")
            else:
                return HttpResponse("Sua Solicitação é Inválida")
        except Exception as e:
            erro = 'Email não Cadastrado! '#+str(e)
    return render(request,'recuperarsenha.html',{'erro':erro})




def suporte(request):
    usuario = request.user
    return render(request,'suporte.html', {'usuario':usuario})


def forcar_user_atualizar_perfil(request):
    usuario = request.user
    perfil = Perfil.objects.get(user=usuario)
    espaco = 0
    numero = 0
    if perfil.nome_completo is None or perfil.email is None :
        return True
    for caracter in perfil.nome_completo:
        if caracter in ' ':
            espaco = espaco + 1
        if caracter in '0123456789':
            numero = numero + 1
    if len(perfil.nome_completo) <10  or len(perfil.email) < 10 or espaco == 0 or numero > 0:
        return True
    return False

############## Usuario #######################
class UserCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'novo_usuario.html'
    success_url = '/perfil/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserCreate, self).get(request, *args, **kwargs)


class UserUpdate(UpdateView):
    model = User
    form_class = UserCreationForm
    #form_class = ProvaForm
    success_url = '/perfil/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserUpdate, self).get(request, *args, **kwargs)

def meuUserUpdate(request):
    erro = ''
    user =request.user
    if  request.method == "POST":
        password = request.POST.get("password")
        #payload = jwt.decode(token, 'wtcs',algorithm='HS256')
        user_senha = authenticate(request=None,username=user.username,password=password)
        if user_senha is None:
            erro = 'Informe sua senha atual. '

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        username = request.POST.get("username")
        if not (password1 == password2) :
            erro = erro + 'Suas senhas não são iguais. '
        numero = 0
        for caracter in password1:
            if caracter in '0123456789':
                numero = numero + 1
        if len(password1) <8 :
            erro = erro + 'Senha muito curta. '
        if len(password1) - numero < 1:
            erro = erro + 'Sua senha não pode ser apenas numerico. '
        if password1 == username:
            erro = erro +'Sua senha não pode ser seu nome de Usuário. '
        if erro != '':
            return render(request,'update_meu_user.html',{'user':user,'erro':erro})

        try:
            #perfil = Perfil.objects.get(user=usuario)
            user.set_password(password1)
            user.username = username
            user.save()
            return redirect('/meu_perfil/')
        except Exception as e:
            erro = str(e)

    return render(request,'update_meu_user.html',{'user':user,'erro':erro})


class UserDelete(DeleteView):
    model = User
    success_url = '/perfil/'
    template_name = 'deleteUser.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(UserDelete, self).get(request, *args, **kwargs)
'''
def user(request):
    user = User.objects.all().order_by('username')
    return render(request,'usuarios.html',{'user':user})

def userDetalhes(request,pk):
    user = User.objects.get(pk=pk)
    return render(request,'usuarios_detalhes.html',{'user':user})
'''


############## Perfil #######################
class PerfilUpdate(UpdateView):
    model = Perfil
    #fields = '__all__'#quais atributos(todos)
    fields = ['user','nome_completo','email','gerenciar_Membros','gerenciar_Grupos_Pequenos','gerenciar_Ministerios','gerenciar_Relatorios','gerenciar_Usuarios']
    #form_class = ProvaForm
    success_url = '/perfil/'
    template_name = 'update_permissoes.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Usuarios:
            return redirect('/sempermissao')
        return super(PerfilUpdate, self).get(request, *args, **kwargs)


def meuPerfilUpdate(request):
    erro = ''
    perfil =request.user.perfil
    if  request.method == "POST":
        nome_completo = request.POST.get("nome_completo")
        email = request.POST.get("email")
        try:
            espaco = 0
            numero = 0
            for caracter in nome_completo:
                if caracter in ' ':
                    espaco = espaco + 1
                if caracter in '0123456789':
                    numero = numero + 1
            if len(nome_completo) <8  or len(email) < 8 or espaco == 0 or numero > 0:
                erro = 'Favor Informar o Nome Completo e Email'
                return render(request,'update_meu_perfil.html',{'perfil':perfil,'erro':erro})
            perfil.nome_completo = nome_completo
            perfil.email = email
            perfil.save()
            return redirect('/meu_perfil/')
        except Exception as e:
            erro = str(e)
    if perfil.nome_completo is None:
         perfil.nome_completo = ''
         perfil.save()
    if perfil.email is None:
         perfil.email = ''
         perfil.save()

    return render(request,'update_meu_perfil.html',{'perfil':perfil,'erro':erro})



def perfil(request):
    if not request.user.perfil.gerenciar_Usuarios:
        return redirect('/sempermissao')
    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    perfil = Perfil.objects.all().order_by('user__username')
    return render(request,'perfil.html',{'perfil':perfil})

def perfilDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Usuarios:
        return redirect('/sempermissao')
    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    perfil = Perfil.objects.get(pk=pk)
    return render(request,'perfil_detalhes.html',{'perfil':perfil})

def meu_perfilDetalhes(request):
    user = request.user.pk
    perfil = Perfil.objects.get(user=user)
    return render(request,'meu_perfil_detalhes.html',{'perfil':perfil})




############## Membro #######################
class MembroCreate(CreateView):
    model = Membro
    fields = '__all__'#quais atributos(todos)
    template_name = 'novo_membro.html'
    success_url = '/membros/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Membros:
            return redirect('/sempermissao')
        return super(MembroCreate, self).get(request, *args, **kwargs)

class MembroUpdate(UpdateView):
    model = Membro
    fields = '__all__'#quais atributos(todos)
    success_url = '/membros/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Membros:
            return redirect('/sempermissao')
        return super(MembroUpdate, self).get(request, *args, **kwargs)

class MembroDelete(DeleteView):
    model = Membro
    success_url = '/membros/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Membros:
            return redirect('/sempermissao')
        return super(MembroDelete, self).get(request, *args, **kwargs)

def membro(request):
    if not request.user.perfil.gerenciar_Membros:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')

    todas_situacao = Situacao.objects.exclude(situacao = 'ATIVO').order_by('situacao')
    situacao_ativo = Situacao.objects.get(situacao = 'ATIVO')
    qtd = 0
    if  request.method == "POST":
        situacao_id = request.POST.get("situacao")
        nome_completo = request.POST.get("nome_completo")
        try:
            situacao = Situacao.objects.get(pk = situacao_id)
            membros = Membro.objects.filter(situacao = situacao, nome_completo__icontains = nome_completo ).order_by('nome_completo')
            qtd = membros.count
        except Exception as e:
            membros = Membro.objects.all().order_by('nome_completo')
            qtd = membros.count

    else:

        #membros = []
        #if opc != 'aniv':
        membros = Membro.objects.filter(situacao = situacao_ativo).order_by('nome_completo')
        qtd = membros.count
    return render(request,'membros.html',{'membros':membros, 'todas_situacao':todas_situacao,'situacao_ativo':situacao_ativo, 'qtd':qtd})


def membroDetalhes(request,pk):
    if not request.user.perfil.gerenciar_Membros:
        return redirect('/sempermissao')


    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')


    try:
        membro = Membro.objects.get(pk=pk)
    except Exception as e:
        return redirect('/membros')
    return render(request,'membro_detalhes.html',{'membro':membro})



def membro_grupo_pequeno_especificoNew(request,pk):
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    erro = ''
    try:
        grupo_pequeno = Grupo_Pequeno.objects.get(pk=pk)
        membros = Membro.objects.all().order_by('nome_completo')
    except Exception as e:
        return redirect('/grupos_pequenos/')
    if  request.method == "POST":
        try:
            id_membro = request.POST.get("membro")
            membro = Membro.objects.get(pk=id_membro)
            membro.grupo_pequeno = grupo_pequeno
            membro.save()
            #return redirect('/membros/')
            return redirect('/grupos_pequenos/'+str(pk)+'/')
        except Exception as e:
            erro = str(e)
            #return JsonResponse({"Erro":"Formulario invalido"},safe=True,status=400)
            return render(request,'novo_membro_grupo_pequeno_especifico.html',{'membros':membros, 'erro':erro,'grupo_pequeno':grupo_pequeno})

    return render(request,'novo_membro_grupo_pequeno_especifico.html',{'membros':membros, 'erro':erro, 'grupo_pequeno':grupo_pequeno})


def membro_grupo_pequenoNew(request):
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    erro = ''
    grupos_pequenos = Grupo_Pequeno.objects.all().order_by('nome')
    membros = Membro.objects.all().order_by('nome_completo')
    if  request.method == "POST":
        try:
            id_membro = request.POST.get("membro")
            id_grupo_pequeno = request.POST.get("grupo_pequeno")
            grupo_pequeno = Grupo_Pequeno.objects.get(pk=id_grupo_pequeno)
            membro = Membro.objects.get(pk=id_membro)
            membro.grupo_pequeno = grupo_pequeno
            membro.save()
            #return redirect('/membros/')
            return redirect('/grupos_pequenos/')
        except Exception as e:
            erro = str(e)
            #return JsonResponse({"Erro":"Formulario invalido"},safe=True,status=400)
            return render(request,'novo_membro_grupo_pequeno.html',{'membros':membros, 'erro':erro,'grupos_pequenos':grupos_pequenos})

    return render(request,'novo_membro_grupo_pequeno.html',{'membros':membros, 'erro':erro, 'grupos_pequenos':grupos_pequenos})


def membro_especifico_no_grupo_pequenoNew(request,pk):
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    erro = ''
    grupos_pequenos = Grupo_Pequeno.objects.all().order_by('nome')
    membro = Membro.objects.get(pk=pk)
    if  request.method == "POST":
        try:
            id_grupo_pequeno = request.POST.get("grupo_pequeno")
            grupo_pequeno = Grupo_Pequeno.objects.get(pk=id_grupo_pequeno)
            membro.grupo_pequeno = grupo_pequeno
            membro.save()
            #return redirect('/membros/')
            return redirect('/grupos_pequenos/'+str(id_grupo_pequeno)+'/')
        except Exception as e:
            erro = str(e)
            return render(request,'atualizar_membro_especifico_do_grupo_pequeno.html',{'membro':membro, 'erro':erro,'grupos_pequenos':grupos_pequenos})

    return render(request,'atualizar_membro_especifico_do_grupo_pequeno.html',{'membro':membro, 'erro':erro, 'grupos_pequenos':grupos_pequenos})






############## Ministerio #######################
class MinisterioCreate(CreateView):
    model = Ministerio
    fields = '__all__'#quais atributos(todos)
    template_name = 'create.html'
    success_url = '/ministerios/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Ministerios:
            return redirect('/sempermissao')
        return super(MinisterioCreate, self).get(request, *args, **kwargs)

class MinisterioUpdate(UpdateView):
    model = Ministerio
    fields = '__all__'#quais atributos(todos)
    success_url = '/ministerios/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Ministerios:
            return redirect('/sempermissao')
        return super(MinisterioUpdate, self).get(request, *args, **kwargs)

class MinisterioDelete(DeleteView):
    model = Ministerio
    success_url = '/ministerios/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Ministerios:
            return redirect('/sempermissao')
        return super(MinisterioDelete, self).get(request, *args, **kwargs)

def ministerio(request):
    if not request.user.perfil.gerenciar_Ministerios:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    ministerios = Ministerio.objects.all().order_by('nome')
    return render(request,'ministerios.html',{'ministerios':ministerios})




def ministerioDetalhes(request,pk):

    if not request.user.perfil.gerenciar_Ministerios:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    try:
        ministerio = Ministerio.objects.get(pk=pk)
        obreiro_Ministerios = Membro.objects.filter(ministerios = ministerio).order_by('nome_completo')
        lider_Ministerios = Membro.objects.filter(ministerios_que_lidera = ministerio).order_by('nome_completo')
        total_obreiros = obreiro_Ministerios.count
    except Exception as e:
        return redirect('/ministerios')
    return render(request,'ministerio_detalhes.html',{'ministerio':ministerio, 'obreiro_Ministerios':obreiro_Ministerios, 'lider_Ministerios':lider_Ministerios, 'total_obreiros':total_obreiros})


################################## Generico #########################################################
def obreiroOuLiderDelete(request,mt,mb,opc):#Deletar o lider ou obreiro
    #opc= 1 é lider
    #opc = 2 é obreiro
    if not request.user.perfil.gerenciar_Ministerios:
        return redirect('/sempermissao')
    try:
        ministerio = Ministerio.objects.get(pk=mt)
        membro = Membro.objects.get(pk=mb)
        if opc == '1':#Lider
            membro.ministerios_que_lidera.remove(ministerio)
        elif opc == '2':#Obreiro
            membro.ministerios.remove(ministerio)
        else:
            return HttpResponse('URL Inválida')
    except Exception as e:
        return redirect('/ministerios/')
    return redirect('/ministerios/'+str(mt)+'/')


def obreiroOuLiderAdicionar(request,mt,mb,opc):
    # mt é id do ministerio ; md é id do membro
    #opc= 1 é lider ministerio
    #opc = 2 é obreiro ministerio
    erro = ''
    ministerio_especifico = ""
    membro_especifico = ""
    if not request.user.perfil.gerenciar_Ministerios:
        return redirect('/sempermissao')
    membros = Membro.objects.all().order_by('nome_completo')
    ministerios = Ministerio.objects.all().order_by('nome')

    try:
        if (opc == '1' or opc == '2') and mt != '0' :#Lider ou Obreiro
            ministerio_especifico = Ministerio.objects.get(pk=mt)
        if  request.method == "POST":
            id_membro = request.POST.get("obreiro")
            id_ministerio = request.POST.get("ministerio")
            ministerio = Ministerio.objects.get(pk=id_ministerio)
            membro = Membro.objects.get(pk=id_membro)

            if opc == '1':#Lider
                membro.ministerios_que_lidera.add(ministerio)
                return redirect('/ministerios/'+str(id_ministerio)+'/')
            elif opc == '2':#Obreiro
                membro.ministerios.add(ministerio)
                return redirect('/ministerios/'+str(id_ministerio)+'/')
            else:
                return HttpResponse('URL Inválida')
    except Exception as e:
        erro = str(e)
    return render(request,'obreiro_ou_lider_adicionar.html',{'ministerios':ministerios, 'membros':membros, 'opc':opc,'erro':erro,'ministerio_especifico':ministerio_especifico})




def liderGrupoPequenoDelete(request,gp,mb):#Deletar o lider do ministerio
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')
    try:
        grupo_pequeno = Grupo_Pequeno.objects.get(pk=gp)
        membro = Membro.objects.get(pk=mb)
        membro.grupos_pequenos_que_lidera.remove(grupo_pequeno)
    except Exception as e:
        return HttpResponse('URL Inválida')
    return redirect('/grupos_pequenos/'+str(gp)+'/')


def liderGrupoPequenoAdicionar(request,gp,mb):
    # mt é id do ministerio ; md é id do membro
    erro = ''
    grupo_pequeno_especifico = ""
    membro_especifico = ""
    if not request.user.perfil.gerenciar_Ministerios:
        return redirect('/sempermissao')
    membros = Membro.objects.all().order_by('nome_completo')
    grupos_pequenos = Grupo_Pequeno.objects.all().order_by('nome')

    try:
        if  gp != '0' :#Lider ou Obreiro
            grupo_pequeno_especifico = Grupo_Pequeno.objects.get(pk=gp)
        if  request.method == "POST":
            id_membro = request.POST.get("obreiro")
            id_grupo_pequeno = request.POST.get("grupo_pequeno")
            grupo_pequeno = Grupo_Pequeno.objects.get(pk=id_grupo_pequeno)
            membro = Membro.objects.get(pk=id_membro)

            membro.grupos_pequenos_que_lidera.add(grupo_pequeno)
            return redirect('/grupos_pequenos/'+str(id_grupo_pequeno)+'/')
    except Exception as e:
        erro = str(e)
    return render(request,'lider_grupo_pequeno_adicionar.html',{'grupos_pequenos':grupos_pequenos, 'membros':membros, 'erro':erro,'grupo_pequeno_especifico':grupo_pequeno_especifico})






############## Grupo Pequeno #######################
class Grupo_PequenoCreate(CreateView):
    model = Grupo_Pequeno
    fields = '__all__'#quais atributos(todos)
    template_name = 'create.html'
    success_url = '/grupos_pequenos/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Grupos_Pequenos:
            return redirect('/sempermissao')
        return super(Grupo_PequenoCreate, self).get(request, *args, **kwargs)

class Grupo_PequenoUpdate(UpdateView):
    model = Grupo_Pequeno
    fields = '__all__'#quais atributos(todos)
    success_url = '/grupos_pequenos/'
    template_name = 'update.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Grupos_Pequenos:
            return redirect('/sempermissao')
        return super(Grupo_PequenoUpdate, self).get(request, *args, **kwargs)

class Grupo_PequenoDelete(DeleteView):
    model = Grupo_Pequeno
    success_url = '/grupos_pequenos/'
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.perfil.gerenciar_Grupos_Pequenos:
            return redirect('/sempermissao')
        return super(Grupo_PequenoDelete, self).get(request, *args, **kwargs)

def grupo_pequeno(request):
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    grupos_pequenos = Grupo_Pequeno.objects.all().order_by('nome')
    return render(request,'grupos_pequenos.html',{'grupos_pequenos':grupos_pequenos})

def grupo_pequenoDetalhes(request,pk):

    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    if forcar_user_atualizar_perfil(request) :
        return redirect('/meu_perfil/update/')
    #try:
    grupo_pequeno = Grupo_Pequeno.objects.get(pk=pk)
    membros = Membro.objects.filter(grupo_pequeno = grupo_pequeno).order_by('nome_completo')
    lider_grupo_pequeno = Membro.objects.filter(grupos_pequenos_que_lidera = grupo_pequeno)
    #except Exception as e:
    #    return redirect('/grupos_pequenos')
    return render(request,'grupo_pequeno_detalhes.html',{'grupo_pequeno':grupo_pequeno, 'membros': membros, 'lider_grupo_pequeno':lider_grupo_pequeno})

###### remover membro do pg ########
def remover_membro_pg(request,pk_m,pk_pg):
    if not request.user.perfil.gerenciar_Grupos_Pequenos:
        return redirect('/sempermissao')

    try:
        membro = Membro.objects.get(pk = pk_m)
        membro.grupo_pequeno = None
        membro.save()
    except Exception as e:
        return redirect('/grupos_pequenos')
    return redirect('/grupos_pequenos/'+str(pk_pg)+'/')
