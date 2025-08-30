from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome', views.welcome, name="welcome"),
    path('users', views.users, name="users"),
]