from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Tb_estoque
from .forms import TbClienteForm, TbUsuarioForm, TbFornecedorForm, TbProdutoForm, Cart
from random import randint

def home(request):
    return render(request, 'home.html')

def calc(request):
    return render(request, 'calc.html')

def success(request):
    return render(request, 'account/success.html')
def successC(request):
    return render(request, 'account/successC.html')

def unsuccessC(request):
    return render(request, 'account/unsuccess/unsuccessC.html')
def unsuccessF(request):
    return render(request, 'account/unsuccess/unsuccessF.html')
def unsuccessU(request):
    return render(request, 'account/unsuccess/unsuccessU.html')
def unsuccessV(request):
    return render(request, 'account/unsuccess/unsuccessV.html')

def cadastro(request):
    if request.method == 'POST':
        form = TbClienteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessC')
    else:
        form = TbClienteForm()
    return render(request, 'account/cadastro.html', {'form': form})

def cadastroU(request):
    if request.method == 'POST':
        form = TbUsuarioForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessU')
    else:
        form = TbUsuarioForm()
    return render(request, 'account/cadastroU.html', {'form': form})

def cadastroF(request):
    if request.method == 'POST':
        form = TbFornecedorForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessF')
    else:
        form = TbFornecedorForm()
    return render(request, 'account/cadastroF.html', {'form': form})

def cadastroP(request):
    if request.method == 'POST':
        form = TbProdutoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessV')
    else:
        form = TbProdutoForm()
    return render(request, 'produtos/produto.html', {'form': form})

def cadastroV(request):
    if request.method == 'POST':
        form = Cart(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../successC')
        else:
            return redirect('../unsuccessV')
    else:
        form = Cart()
    return render(request, 'account/cadastroV.html', {'form': form})