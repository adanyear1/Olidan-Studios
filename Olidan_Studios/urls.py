"""
Definition of urls for Olidan_Studios.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('guests/', views.guests, name='guests'),
    path('episodes/', views.media, name='media'),
    path('admin/', admin.site.urls),
]
