from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('branch/',views.branch,name="branch"),
    path('branch_ifsc/<ifsc>',views.branch_ifsc,name="branch_ifsc"),
    path('bank_name_city/<name>/<city>',views.bank_name_city,name="bank_name_city"),
    path('bank/',views.bank,name="bank"),
    
]