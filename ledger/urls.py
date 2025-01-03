from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ledger, name= 'ledger'),
   # path('logbook/', views.logbook, name='logbook'),
]