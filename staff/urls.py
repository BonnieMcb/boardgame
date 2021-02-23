from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/edit/', views.edit_product, name='edit_product'),
    path('shop/remove/', views.remove_product, name='remove_product'),
]
