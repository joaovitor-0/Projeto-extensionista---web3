from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('contato/', views.contato, name='contato'),
    path('transparencia/', views.transparencia, name='transparencia'),
]