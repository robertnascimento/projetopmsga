from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome Completo', max_length=100,blank=False)
    idade = models.IntegerField('Idade',blank=False)
    cpf = CPFField(masked=True,blank=False,unique=True)

    USERNAME_FIELD = 'cpf'

    class Meta:
        permissions = [
            ("CD","Cadastrar,Apagar"),
            ("RU","Lerd,Atualizar")
        ]

    def __str__(self):
        return self.nome.upper()


class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=100,blank=False)
    cnpj = CNPJField(masked=True,blank=False)
    telefone = models.IntegerField('Telefone',blank=False)
    codigoPostal = models.IntegerField('CEP',blank=False)
    emailFornecedor = models.EmailField('Email',max_length=100,blank=False)
    fotoFornecedor = models.ImageField('Foto',upload_to='fornecedoresImg',null=True)

    def __str__(self):
        return self.nome.upper()

class TipoProduto(models.Model):
    nome = models.CharField('Nome',max_length=20,blank=False)

    def __str__(self):
        return self.nome.upper()

class Produto(models.Model):
    modelo = models.CharField('Nome',max_length=30,blank=False)
    quantidade = models.IntegerField('Quantidade',blank=False)
    fotoUm = models.ImageField('Foto',upload_to='fotosProduto',blank=False)
    fotoDois = models.ImageField('Foto',upload_to='fotosProduto',blank=True)
    fotoTres = models.ImageField('Foto',upload_to='fotosProduto',blank=True)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
    equipamento = models.ForeignKey(TipoProduto,on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo.upper()


class Retiradas(models.Model):
    quantidaderet = models.IntegerField('Quantidade',blank=False)
    nome = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    data = models.DateTimeField(default='2022-01-01 01:00:00 +00:00')
    
class Entradas(models.Model):
    quantidadeent = models.IntegerField('Quantidade',blank=False)
    nome = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    data = models.DateTimeField(default='2022-01-01 01:00:00 +00:00')