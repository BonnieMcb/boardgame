from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/edit/', views.product_list, name='product_list'),
    path('shop/edit/<product_id>', views.edit_product, name='edit_product'),
    path('shop/edit/commit/<prod_id>', views.commit_edit, name='commit_edit'),
    path('shop/remove/', views.remove_product, name='remove_product'),
]
