from django.shortcuts import render
from .models import Product

# Create your views here.


def all_games(request):

    games = Product.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)
