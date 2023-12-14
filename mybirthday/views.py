from django.shortcuts import render
from .forms import AniversarioForm
from django.utils import timezone


# Create your views here.
def verificar_aniversario(request):
    mensagem = ''  # Defina uma mensagem padrão
    
    if request.method == 'POST':
        form = AniversarioForm(request.POST)
        if form.is_valid():
            data_aniversario = form.cleaned_data['data_aniversario']
            hoje = timezone.now().date()
            
            if data_aniversario.month == hoje.month and data_aniversario.day == hoje.day:
                return render(request, 'feliz_aniversario.html')  # Redireciona para página de feliz aniversário
            else:
                mensagem = 'Hoje não é o seu aniversário. 😢'
    else:
        form = AniversarioForm()

    return render(request, 'verificar_aniversario.html', {'form': form, 'mensagem': mensagem})