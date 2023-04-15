from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from django.views import View

class Index(View):
    template_name = 'pages/index.html'
    def get(self, request):

        prods = models.produto.objects.all()
        prods_dic = {
            "prods" : prods,
            "home" : "Home"
            }

        return render(request, self.template_name, prods_dic)

class Login(View):
    template_name = 'pages/login.html'
    form = forms.LoginForm()
    context = {"form" : form}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = forms.LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index")
