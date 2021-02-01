from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Mechanic
from .models import Category

# Create your views here.


def all_games(request):
    """ A view to show all products """

    games = Product.objects.all().order_by('rank')  # Ignore lint error

    paginator = Paginator(games, 48)  # Show 48 games per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    return render(request, 'games/games.html', {
        'page_obj': page_obj, 'mechanics': mechanics,
        'categories': categories})


def game_detail(request, game_id):
    """ A view to show individual product details """

    game = get_object_or_404(Product, pk=game_id)

    context = {
       'product': game
    }

    return render(request, 'games/game_detail.html', context)
