from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product
from .models import Mechanic
from .models import Category

# Create your views here.


def all_games(request):
    """ A view to show all products """

    games = Product.objects.all().order_by('rank')  # Ignore lint
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
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

    # add product categories for printing in template
    for product in page_obj:
        product.categories = product.category_id.all()
        product.mechanics = product.mechanic_id.all()

    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    current_sorting = f'{sort}_{direction}'

    context = {
        'page_obj': page_obj,
        'mechanics': mechanics,
        'categories': categories,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to show individual product details """

    game = get_object_or_404(Product, pk=game_id)

    game.categories = game.category_id.all()
    game.mechanics = game.mechanic_id.all()

    mechanics = Mechanic.objects.all()
    categories = Category.objects.all()

    context = {
       'product': game,
       'mechanics': mechanics,
       'categories': categories,
    }

    return render(request, 'games/game_detail.html', context)
