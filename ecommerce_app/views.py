from django.shortcuts import render
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):

    prods = models.produto.objects.all()
    prods_dic = {
        "prods" : prods,
        "home" : "Home"
        }
    
    return render(request, 'pages/index.html', prods_dic)

