from django.shortcuts import render
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):

    prods = models.produto.objects.all()
    prods_dic = {
        "prods" : prods,
        "home" : "Home"
        }
    
    return render(request, 'main/index.html', prods_dic)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        