from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib import messages
from .models import Fornecedor, TipoProduto , Produto, Usuario, Retiradas
from .forms import FornecedorForm, TipoProdutoForm, ProdutoForm, UsuarioCreationForm, RetiradaForm


@login_required
def home(request):
    return render(request,'home.html')


@login_required
def perfil(request):
    return render(request,'perfil.html')



def registro(request):
    form = UsuarioCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    
    return render(request,'registro.html',contexto)

def dados(request,id):
    user = Usuario.objects.get(pk=id)

    form = UserCreationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('perfil')

    contexto = {
        'form': form
    }
    return render(request, 'dadosEdit.html', contexto)



"""
FORNECEDORES
"""
@login_required
def fornecedor_lista(request):
    fornec = Fornecedor.objects.all()
    contexto = {
        'list_fornecedor': fornec
    }
    return render(request,'fornecedor_lista.html',contexto)

@login_required
def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')

    contexto = {
        'form': form
    }

    return render(request,'fornecedorcad.html',contexto)

@login_required
def fornecedor_Edit(request,id):
    frnc = Fornecedor.objects.get(pk=id)
    
    form = FornecedorForm(request.POST or None,request.FILES or None, instance=frnc)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    
    contexto = {
        'form': form
    }

    return render(request, 'fornecedor_edit.html', contexto)

@login_required
def fornecedor_remover(request, id):
    frnc = Fornecedor.objects.get(pk=id)
    frnc.delete()
    return redirect('list_fornecedor')



"""
TIPO PRODUTOS
"""

@login_required
def tipoProduto_Lista(request):
    tpProd = TipoProduto.objects.all()
    contexto = {
        'list_tipoProduto': tpProd
    }
    return render(request,'tipoprodutolista.html',contexto)

@login_required
def tipoProduto_Cadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if form.is_valid():
        upperCase = request.POST['nome']
        form.nome = upperCase.upper()
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form' : form
    }

    return render(request,'tipoprodutocad.html',contexto)

@login_required
def tipoProduto_Edit(request,id):
    tprd = TipoProduto.objects.get(pk=id)

    form = TipoProdutoForm(request.POST or None,instance= tprd)
    if form.is_valid():
        form.save()
        return redirect('list_tipoProduto')

    contexto = {
        'form' : form
    }

    return render(request,'tipoprodutoedit.html',contexto)

@login_required
def tipoProduto_Remover(request,id):
    tprd = TipoProduto.objects.get(pk=id)
    tprd.delete()
    return redirect('list_tipoProduto')



"""
PRODUTOS
"""

@login_required
def produto_lista(request):
    prod = Produto.objects.all()
    contexto = {
        'list_produto': prod
    }
    return render(request,'produto_lista.html',contexto)

@login_required
def produto_cadastro(request):
    form = ProdutoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_cad.html',contexto)

@login_required
def produto_edit(request,id):
    prd = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None,request.FILES or None,instance=prd)
    if form.is_valid():
        form.save()
        return redirect('list_produto')

    contexto = {
        'form': form
    }
    return render(request,'produto_edit.html',contexto)

@login_required
def produto_remover(request,id):
    prd = Produto.objects.get(pk=id)
    prd.delete()
    return redirect('list_produto')

def retiradas(request,id):
    prod = Produto.objects.get(pk=id)
    form = RetiradaForm(request.POST or None)

    if form.is_valid():
        qtd = request.POST['quantidaderet']
        qtdInt = int(qtd)
        if prod.quantidade == 0:
            messages.error(request,"Não tem produtos no estoque")
        elif qtdInt <= 0:
            messages.error(request,"Digite uma quantidade válida")
        elif qtdInt <= prod.quantidade:

            prod.quantidade -= qtdInt
            messages.success(request,"Retirada realizada com sucesso")
            form.save()
            prod.save()
        else:
            messages.info(request,"Quantidade solicitada, maior do que à quantidade disponível")
    
        return redirect('list_produto')


    contexto = {
        'form': form
    }

    return render(request,'retirada.html',contexto)

"""
RETIRADAS REALIZADAS
"""
def retiradasrealizadas(request):
    rtrd = Retiradas.objects.all()
    contexto = {
        'rtrok': rtrd
    }
    return render(request,'retiradasrealizadas.html',contexto)
"""
DELETAR RETIRADAS REALIZADAS
"""
def retreal_remover(request, id):
    rtr = Retiradas.objects.get(pk=id)
    rtr.delete()
    messages.error(request,"Retirada apagada")
    return redirect('rtrok')