from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('cart/<int:id>/', views.cart, name="cart"),
    path('cartvalue/', views.cartvalue),
    path('cartcalculate/', views.cartcalculate)
]
