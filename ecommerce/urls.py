from django.contrib import admin
from django.urls import path

from ecommerce import views

urlpatterns = [
    path('home/', views.home),
]
