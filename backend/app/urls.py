from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects')

]
