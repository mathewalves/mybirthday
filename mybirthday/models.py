from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_aniversario = models.DateField(null=True, blank=True)