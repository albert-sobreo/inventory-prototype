from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('loginprocess/', views.loginprocess),
    path('logout/', views.logout),
    path('register/', views.register),
    path('registerprocess/', views.registerprocess)
]
