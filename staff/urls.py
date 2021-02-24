from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/add/commit/', views.commit_add, name='commit_add'),
    path('shop/edit/', views.product_list, name='product_list'),
    path('shop/edit/<product_id>', views.edit_product, name='edit_product'),
    path('shop/edit/commit/<prod_id>', views.commit_edit, name='commit_edit'),
    path('shop/remove/', views.remove_product, name='remove_product'),

    path('event/add/', views.add_event, name='add_event'),
    path('event/add/commit/', views.commit_add_event, name='commit_add_event'),
    path('event/edit/', views.events_list, name='event_list'),
    path('event/edit/<event_id>', views.edit_event, name='edit_event'),
    path('event/edit/commit/<event_id>', views.commit_edit_event, name='commit_edit_event'),
    path('event/remove/', views.remove_event, name='remove_event'),
]
