from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product
from .models import Mechanic
from .models import Category

from decimal import *
from bag.contexts import get_discount

# Create your views here.


def all_games(request):
    """ A view to show all products """

    games = Product.objects.all().order_by('rank')  # Ignore lint
    query = None
    categories = None
    sort = None
    direction = None

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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                games = games.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            games = games.order_by(sortkey)

    # apply membership discounts if needed
    discount = get_discount(request)
    if discount < 1.0:
        for game in games:
            game.discounted_price = round(discount * float(game.price), 2)

    paginator = Paginator(games, 48)  # Show 48 games per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # To pass through the cats and mechs for each game
    for product in page_obj:
        product.categories = product.category_id.all()
        product.mechanics = product.mechanic_id.all()

    # To create the sidebar links
    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    current_sorting = f'{sort}_{direction}'

    # To create the sorting URLs
    # With help from: https://stackoverflow.com/questions/11280948/best-way-to-get-query-string-from-a-url-in-python
    # and https://stackoverflow.com/questions/4591525/is-it-possible-to-pass-query-parameters-via-djangos-url-template-tag
    get_params = ''
    url_params = request.GET.urlencode()
    if url_params:
        get_params = url_params + '&'

    context = {
        'page_obj': page_obj,
        'mechanics': mechanics,
        'categories': categories,
        'search_term': query,
        'get_params': get_params,
        'current_sorting': current_sorting
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to show individual product details """

    game = get_object_or_404(Product, pk=game_id)

    # To pass through the cats and mechs for each game
    game.categories = game.category_id.all()
    game.mechanics = game.mechanic_id.all()

    # To create the sidebar links
    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    context = {
       'product': game,
       'mechanics': mechanics,
       'categories': categories,
    }

    return render(request, 'games/game_detail.html', context)
