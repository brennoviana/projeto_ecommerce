from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    prods = models.produto.objects.all()
    prods_dic = {"prods" : prods}
    return render(request, 'pages/index.html', prods_dic)