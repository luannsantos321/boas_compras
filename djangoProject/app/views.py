from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoForm
# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def cadastro(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request,'cadastro.html', {'form':form})



def lista(request):
    preco = request.POST.get('preco')

    lista = Produto.objects.all()
    dados = {'lista': lista, 'preco': preco}
    return render(request, 'lista.html', dados)

def update_lista(request, id):
    lista = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=lista)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cadastro.html', {'lista': lista, 'form':form})

def delete_id_lista(request, id):
    lista = Produto.objects.get(id=id)

    if request.method == 'POST':
        lista.delete()
        return redirect('lista')
    return render(request, 'cadastro.html')

def delete_lista(request):
    lista = Produto.objects.all()

    if request.method == 'POST':
        lista.delete()
        return redirect('lista')
    return render(request, 'cadastro.html')

