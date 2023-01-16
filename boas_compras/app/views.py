from django.shortcuts import render,redirect
from .models import Produto
from .forms import ProdutoForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'cadastro.html', {'form':form})

def lista(request):
    lista = Produto.objects.all()
    dados = {'lista': lista}
    return render(request, 'inicio.html',dados)
