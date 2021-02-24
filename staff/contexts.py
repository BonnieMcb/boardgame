from django.core.paginator import Paginator
from games.models import Product
from events.models import Events


def is_staff(request):

    # TODO: DEBUG ONLY
    return True

    user = request.user
    if user.is_authenticated:
        return False

    # TODO: another metric for staff access?
    return user.is_superuser()


def shop_list(request):
    games = Product.objects.all()

    paginator = Paginator(games, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


def event_list(request):
    events = Events.objects.all()

    paginator = Paginator(events, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj

