from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

# Create your views here.


def all_games(request):

    games = Product.objects.all().order_by('rank')  # Ignore the

    paginator = Paginator(games, 16)  # Show 16 games per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'games/games.html', {'page_obj': page_obj})
