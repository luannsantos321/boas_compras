from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Produto,Valor
from .forms import ProdutoForm, ValorForm
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def lista(request):
    lista = Produto.objects.all()
    valor = Valor.objects.all()
    return render(request, 'lista.html', {'lista': lista, 'valor': valor})


def cadastro(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'cadastro.html', {'form': form, })


def update_produto(request,id):
    lista = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=lista)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cadastro.html', {'form': form, 'lista': lista})


def delete_produto(request, id):
    lista = Produto.objects.get(id=id)

    if request.method == 'POST':
        lista.delete()
        return redirect('lista')
    return render(request, 'cadastro.html')

def delete_produto_all(request):
    lista = Produto.objects.all()

    if request.method == 'POST':
        lista.delete()
        return redirect('lista')
    return render(request, 'cadastro.html')
'''---------------------------------------------'''

def cadastro_valor(request):
    form2 = ValorForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        return redirect('lista')
    return  render(request, 'cadastro_valor.html',{'form2': form2})

def delete_valor(request, id):
    valor = Valor.objects.get(id=id)

    if request.method == 'POST':
        valor.delete()
        return redirect('lista')
    return render(request, 'cadastro_valor.html')

def soma(request):
    valor = Valor.objects.all()
    total = 0.00
    for valor in valor:
        total += valor
    return HttpResponse(request, 'lista.html', {'total': total})
