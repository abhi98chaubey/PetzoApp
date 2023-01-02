from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('howItWork/', views.howItWork),
    path('careers/', views.careers),
    path('howItWork/', views.howItWork),
    path('partnerships/', views.partnerships),
    path('blog/', views.blog),
    path('login/', views.login),
    path('downloadApp/', views.downloadApp),
]
