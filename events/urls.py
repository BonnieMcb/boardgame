from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('sign/<event_id>', views.sign, name='sign'),
    path('unsign/<event_id>', views.unsign, name='unsign')
]
 