from django.db import models
from datetime import date
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Trilha_Discipulado(models.Model):
    trilha_discipulado = models.CharField(max_length=100,unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return str(self.trilha_discipulado)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.trilha_discipulado = self.trilha_discipulado.upper()
        super(Trilha_Discipulado, self).save(force_insert, force_update)


class Situacao(models.Model):
    situacao = models.CharField(max_length=100,unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return str(self.situacao)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.situacao = self.situacao.upper()
        super(Situacao, self).save(force_insert, force_update)

class Grupo_Pequeno(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return str(self.nome)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        super(Grupo_Pequeno, self).save(force_insert, force_update)

class Origem(models.Model):
    origem = models.CharField(max_length=30,unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return str(self.origem)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.origem = self.origem.upper()
        super(Origem, self).save(force_insert, force_update)



class Sexo(models.Model):
    sexo = models.CharField(max_length=10,unique=True)
    def __str__(self):
        return str(self.sexo)


class Uf(models.Model):
    uf = models.CharField(max_length=2,unique=True)
    estado = models.CharField(max_length=30,unique=True)
    #estado = models.CharField(max_length=30)
    def __str__(self):
        return str(self.uf)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.uf = self.uf.upper()
        super(Uf, self).save(force_insert, force_update)



class Estado_Civil(models.Model):
    estado_civil = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return str(self.estado_civil)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.estado_civil = self.estado_civil.upper()
        super(Estado_Civil, self).save(force_insert, force_update)


class Escolaridade(models.Model):
    escolaridade = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return str(self.escolaridade)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.escolaridade = self.escolaridade.upper()
        super(Escolaridade, self).save(force_insert, force_update)



class Membro(models.Model):
    nome_completo = models.CharField(max_length=100 )
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT)
    data_situacao = models.DateField(blank=True,null=True)
    data_nascimento = models.DateField(default=datetime.now,blank=True,null=True)
    naturalidade = models.CharField(max_length=30,blank=True)
    uf_nascimento = models.ForeignKey(Uf, related_name = 'uf_nascimento', on_delete=models.PROTECT,null=True,blank=True)
    cpf = models.CharField(max_length=11,blank=True)
    rg = models.CharField(max_length=15,blank=True)
    endereco = models.CharField(max_length=50,blank=True)
    n = models.CharField(max_length=10,blank=True)
    bairro = models.CharField(max_length=50,blank=True)
    cidade = models.CharField(max_length=50)
    uf_endereco = models.ForeignKey(Uf, related_name = 'uf_endereco', on_delete=models.PROTECT)
    cep = models.CharField(max_length=10,blank=True)
    telefone_celular = models.CharField(max_length=15,blank=True)
    telefone_residencial = models.CharField(max_length=15,blank=True)
    telefone_comercial = models.CharField(max_length=15,blank=True)
    email = models.EmailField(max_length=254,blank=True)
    nome_responsavel = models.CharField(max_length=100,blank=True)
    estado_civil = models.ForeignKey(Estado_Civil, on_delete=models.PROTECT)
    nome_conjuge = models.CharField(max_length=100,blank=True)
    data_casascimento = models.DateField(blank=True,null=True)

    numero_filhos = models.PositiveIntegerField(default= 0)
    filho1 = models.CharField(max_length=100,blank=True)
    data_nascimento_filho1 = models.DateField(blank=True,null=True)
    filho2 = models.CharField(max_length=100,blank=True)
    data_nascimento_filho2 = models.DateField(blank=True,null=True)
    filho3 = models.CharField(max_length=100,blank=True)
    data_nascimento_filho3 = models.DateField(blank=True,null=True)
    outros_filhos = models.TextField(blank=True)

    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT)
    profisao = models.CharField(max_length=50,blank=True)
    economicamente_ativo = models.BooleanField(default = False)

    data_conversao = models.DateField(default=datetime.now,blank=True,null=True)
    data_batismo = models.DateField(default=datetime.now,blank=True,null=True)
    igreja_batismo = models.CharField(max_length=50,blank=True)
    pastor = models.CharField(max_length=100,blank=True)
    data_chegada_na_elshaday = models.DateField(default=datetime.now,blank=True,null=True)
    origem = models.ForeignKey(Origem, on_delete=models.PROTECT,blank=True,null=True)
    ministerios_que_deseja_participar = models.CharField(max_length=100, blank=True)
    participa_grupo_pequeno = models.BooleanField(default = False)
    grupo_pequeno = models.ForeignKey(Grupo_Pequeno, on_delete=models.PROTECT,blank=True,null=True)

    trilha_discipulado = models.ManyToManyField(Trilha_Discipulado, blank=True)

    obs = models.TextField(blank=True)

    def __str__(self):
        return str(self.nome_completo)
    #funcao que faz com que os campos sejam Maiusculo automaticamente
    def save(self, force_insert=False, force_update=False):
        self.nome_completo = self.nome_completo.upper()
        super(Membro, self).save(force_insert, force_update)


class Lider_Grupo_Pequeno(models.Model):
    lider = models.ForeignKey(Membro,related_name = 'lider', on_delete=models.CASCADE)
    grupo_pequeno = models.ForeignKey(Grupo_Pequeno, on_delete=models.CASCADE)
    obs = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.lider) +' LIDER DO(A) '+ str(self.grupo_pequeno )



class Ministerio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    areas_atuacao = models.CharField(max_length=100,blank=True)
    obs = models.TextField(blank=True)
    def __str__(self):
        return str(self.nome)

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        super(Ministerio, self).save(force_insert, force_update)

class Lider_Ministerio(models.Model):
    nome_lider = models.ForeignKey(Membro,related_name = 'nome_lider', on_delete=models.CASCADE)
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)
    obs = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.nome_lider) +' LIDER DO '+ str(self.ministerio )

    '''
    def save(self, force_insert=False, force_update=False):
        try:
            x = Lider_Ministerio.objects.get(ministerio = self.ministerio, nome_lider = self.nome_lider )
        except Exception as e:
            super(Lider_Ministerio, self).save(force_insert, force_update)
            #So salva se nao tiver nenhum ingual
        #nao faz nada se tiver repetido
    '''

class Obreiro_Ministerio(models.Model):
    obreiro = models.ForeignKey(Membro,related_name = 'obreiro', on_delete=models.CASCADE)
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)
    obs = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.obreiro) +' OBREIRO DO '+ str(self.ministerio )



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    gerenciar_Membros = models.BooleanField(default = False)
    gerenciar_Grupos_Pequenos = models.BooleanField(default = False)
    gerenciar_Ministerios = models.BooleanField(default = False)
    gerenciar_Relatorios = models.BooleanField(default = False)
    gerenciar_Usuarios = models.BooleanField(default = False)
    recuperar = models.CharField(max_length=100,blank=True,null=True)
    data_recuperar = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.user.username

#usar isso para criar automaticamente um perfil
@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
#usar isso para criar automaticamente um perfil
@receiver(post_save, sender=User)
def save_user_perfil(sender, instance, **kwargs):
    instance.perfil.save()
