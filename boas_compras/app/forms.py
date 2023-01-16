from django.forms import forms
from .models import Produto
class ProdutoForm(forms.Form):
    class Meta:
        model = Produto

    fields = ['produto']
