from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('searchForm/', views.SearchProd.as_view(), name='searchForm'),
    path('prod/<int:prod_id>/', views.ProdView.as_view(), name='prodSearch')
]
