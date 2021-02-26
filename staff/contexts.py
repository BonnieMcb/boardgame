from django.core.paginator import Paginator
from games.models import Product
from events.models import Events
from django.db.models import Q


DEFAULT_ITEMS_PER_PAGE = 25


def is_staff(request):

    # TODO: DEBUG ONLY
    return True

    user = request.user
    if user.is_authenticated:
        return False

    # TODO: another metric for staff access?
    return user.is_superuser()


# cut down version of the function from games view
def handle_url_params(request):

    base = request.GET.urlencode() + '&'
    get_params = {
        'no_page': base,
        'no_count': base,
        'search': ''
    }

    url_params = request.GET.urlencode()
    if url_params:

        # remove params as needed
        has_page = 'page' in request.GET
        has_count = 'count' in request.GET
        has_q = 'q' in request.GET

        if has_page:
            copy = request.GET.copy()
            copy.pop('page')
            get_params['no_page'] = copy.urlencode() + '&'

        if has_count:
            copy = request.GET.copy()
            copy.pop('count')
            if has_page:
                copy.pop('page')
            get_params['no_count'] = copy.urlencode() + '&'

        if has_q:
            get_params['search'] = request.GET.get('q')

    return get_params


def shop_list(request):
    games = Product.objects.all()

    items_per_page = DEFAULT_ITEMS_PER_PAGE
    param_count = request.GET.get('count')
    if param_count:
        items_per_page = param_count

    query = request.GET.get('q')
    if query:
        query_set = Q(names__icontains=query)
        games = games.filter(query_set)

    paginator = Paginator(games, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


def event_list(request):
    events = Events.objects.all()

    items_per_page = DEFAULT_ITEMS_PER_PAGE
    param_count = request.GET.get('count')
    if param_count:
        items_per_page = param_count

    query = request.GET.get('q')
    if query:
        query_set = Q(name__icontains=query)
        events = events.filter(query_set)

    paginator = Paginator(events, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj

