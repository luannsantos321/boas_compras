from django.shortcuts import render,redirect
from .models import Produto
from .forms import ProdutoForm
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def lista(request):
    lista = Produto.objects.all()
    return render(request, 'lista.html', {'lista': lista})


def cadastro(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cadastro.html', {'form': form})

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
    return render(request, 'lista.html', {'lista': lista})
