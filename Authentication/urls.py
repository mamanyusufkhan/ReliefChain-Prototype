from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('donorLogin/', views.donor_login),
    path('donorRegister/', views.donor_register),
    path('donorLogout/', views.donor_logout, name="donorLogout"),
    path('fundRaiserLogin/', views.fundRaiser_login),
    path('fundRaiserRegister/', views.fundRaiser_register),
    path('fundRaiserLogout/', views.fundRaiser_logout, name="fundRaiserLogout"),
    path('adminLogin/', views.admin_login),
    path('adminRegister/', views.admin_register),
    path('adminLogout/', views.admin_logout, name="adminLogout"),

    
]