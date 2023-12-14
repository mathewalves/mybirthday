from django import forms
from .models import Perfil

class AniversarioForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['data_aniversario']
        widgets = {
            'data_aniversario': forms.DateInput(attrs={'type': 'date'}),
        }