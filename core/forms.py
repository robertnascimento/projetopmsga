from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Fornecedor,TipoProduto,Produto, Usuario, Retiradas, Entradas

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','cnpj','telefone','codigoPostal','emailFornecedor','fotoFornecedor']

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['modelo','quantidade','fornecedor','equipamento','fotoUm','fotoDois','fotoTres']

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','password1','password2','cpf','email','nome','idade']

class RetiradaForm(forms.ModelForm):
    class Meta:
        model = Retiradas
        fields = ['quantidaderet','nome']

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['quantidadeent']