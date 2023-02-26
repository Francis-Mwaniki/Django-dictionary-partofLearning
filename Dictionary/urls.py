""" urlpattern for Dictionary app """
from django.urls import path
from . import views

urlpatterns = [
     path('', views.homeView, name='home'),#this is the home url
    path('search', views.searchView, name='search'),#this is the search url
    
]