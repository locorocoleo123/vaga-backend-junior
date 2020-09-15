from django.contrib import admin
from .models import Clube, Jogo


# Register your models here.
my_models = [Clube,Jogo]  # iterable list
admin.site.register(my_models)