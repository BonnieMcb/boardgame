from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='games'),
    path('<game_id>', views.game_detail, name='game_detail'),
]
