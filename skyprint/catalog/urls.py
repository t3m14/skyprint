from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('catalog', views.catalog, name='catalog'),
]
