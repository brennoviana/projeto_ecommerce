﻿from django.shortcuts import render, redirect, HttpResponse
from . import models
from . import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
import json
from django.http import JsonResponse
from django.template.loader import render_to_string


from django.views import View

class Index(View):
    template_name = 'pages/index.html'
    def get(self, request):

        prods = models.prod.objects.all().order_by('-created_at')
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
        else:
            messages.warning(request, 'UsuÃ¡rio nÃ£o autorizado')
            return redirect('login')
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index")

class SearchProd(View):
    def post(self, request):
        q = json.loads(request.body)
        prods2 = models.prod.objects.filter(name_prod__icontains=q.get("querry")) if q else models.prod.objects.all()
        html_results = render_to_string('pages/index.html', {'prods': prods2})
        return JsonResponse({'html_results': html_results})