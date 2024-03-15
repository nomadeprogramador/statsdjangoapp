from django import forms
from .models import Categoria,Despesa


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields=['nome','descricao']
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields=['nome','valor','categoria','data','descricao']
        widgets={
            'data':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self,user,*args,**kwargs):
        super(DespesaForm,self).__init__(*args,**kwargs)
        self.fields['categoria'].queryset= Categoria.objects.filter(usuario=user)