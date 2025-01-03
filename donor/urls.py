from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate', views.donate, name='donate'),
    path('checkmodalvalue/', views.checkmodalvalue, name='checkmodalvalue'),
]
