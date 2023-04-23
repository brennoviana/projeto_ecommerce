from django.shortcuts import render, redirect, HttpResponse
from . import models
from . import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
import json
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views import View

class Index(View):
    template_name = 'pages/index.html'
    def get(self, request):
        prods = models.prod.objects.all().order_by('-created_at')
        prods_dic = {"prods" : prods}
        return render(request, self.template_name, prods_dic)

class Login(View):
    template_name = 'pages/login.html'
    form = forms.LoginForm
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
            messages.warning(request, 'Usuário não autorizado')
            return redirect('login')
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index")

class SearchProd(View):
    def post(self, request):
        q = json.loads(request.body)
        if q.get("querry") == "":
            html_results = render_to_string('partials/search.html')    
            return JsonResponse({'html_results': html_results})
        prods2 = models.prod.objects.filter(name_prod__icontains=q.get("querry"))[:10]
        html_results = render_to_string('partials/search.html', {'prods2': prods2, 'request': request})
        return JsonResponse({'html_results': html_results})
    

class ProdView(View):
    template_name = 'pages/prod.html'
    def get(self, request, prod_id):
        produto = models.prod.objects.filter(id=prod_id)
        prod = {"produto" : produto}
        return render(request, self.template_name, prod)
    
class Estoque(View):
    def get(self, request):
        prodForm = forms.ProdForm
        return render(request, 'pages/estoque.html', {"form" : prodForm})
    
    def post(self, request):
        prodForm = forms.ProdForm(request.POST, request.FILES)
        if prodForm.is_valid():
            prodForm.save()
        return redirect('estoque')