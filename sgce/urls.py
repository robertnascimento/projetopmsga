"""sgce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import retreal_remover,retiradasrealizadas,retiradas,perfil,dados,fornecedor_lista,fornecedor_Edit,fornecedor_cadastro,fornecedor_remover, tipoProduto_Edit,tipoProduto_Cadastro,tipoProduto_Lista
from core.views import produto_lista, produto_edit, produto_cadastro, produto_remover, registro,tipoProduto_Remover,home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',home,name='home'),

    path('perfil/',perfil,name='perfil'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('registro/',registro ,name='registro'),
    path('dados/<int:id>/',dados,name='edit_dados'),

    path('fornecedorCad/',fornecedor_cadastro,name='cad_fornecedor'),
    path('fornecedorList/',fornecedor_lista,name='list_fornecedor'),
    path('fornecedorEdit/<int:id>',fornecedor_Edit,name='edit_fornecedor'),
    path('fornecedorDelete/<int:id>',fornecedor_remover,name='fornecedor_remover'),

    path('tipoProdutoCad/',tipoProduto_Cadastro,name='cad_tipoProduto'),
    path('tipoProdutoList/',tipoProduto_Lista,name='list_tipoProduto'),
    path('tipoProdutoEdit/<int:id>',tipoProduto_Edit,name='edit_tipoProduto'),
    path('tipoProdutoDelete/<int:id>',tipoProduto_Remover,name='del_tipoProduto'),

    path('produtoList/',produto_lista,name='list_produto'),
    path('produtoCad/',produto_cadastro,name='cad_produto'),
    path('produtoEdit/<int:id>',produto_edit,name='edit_produto'),
    path('produtoDelete/<int:id>',produto_remover,name='del_produto'),

    path('retirada/<int:id>/',retiradas,name='retiradas'),
    path('retiradasrealizadas/',retiradasrealizadas,name='rtrok'),
    path('retiradasrealizadas/<int:id>',retreal_remover,name='rtrdel'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

