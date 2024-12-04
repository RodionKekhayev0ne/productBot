from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list),
    path('create/', views.create_product, name='create_product'),


]
