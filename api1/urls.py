from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('branch/',views.branch,name="post"),
    path('bank/',views.bank,name="post"),
    
]