from django.urls import path
from .views import verificar_aniversario

from . import views

urlpatterns = [
    path('verificar-aniversario/', verificar_aniversario, name='verificar_aniversario'),
]