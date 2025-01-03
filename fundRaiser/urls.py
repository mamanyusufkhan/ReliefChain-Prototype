from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('donate', views.donate, name='donate')
  
]
