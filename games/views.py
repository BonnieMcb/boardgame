from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .models import Mechanic
from .models import Category

# Create your views here.


def all_games(request):
    """ A view to show all products """

    games = Product.objects.all().order_by('rank')  # Ignore lint
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']

            games = games.filter(category_id__name__exact=category)

        if 'mechanic' in request.GET:
            mechanic = request.GET['mechanic']

            games = games.filter(mechanic_id__name__exact=mechanic)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search terms.")
                return redirect(reverse('games'))

            queries = Q(names__icontains=query)
            games = games.filter(queries)

    paginator = Paginator(games, 48)  # Show 48 games per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'mechanics': mechanics,
        'categories': categories,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to show individual product details """

    game = get_object_or_404(Product, pk=game_id)

    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    context = {
       'product': game,
       'mechanics': mechanics,
       'categories': categories,
    }

    return render(request, 'games/game_detail.html', context)
