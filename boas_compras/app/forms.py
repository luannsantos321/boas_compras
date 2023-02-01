from django import forms
from .models import Produto, Valor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class ValorForm(forms.ModelForm):
    class Meta:
        model = Valor
        fields = ['valor']