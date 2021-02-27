from django.shortcuts import render

from django.db.models import Max
import random

from events.models import Events
from games.models import Product


def index(request):

    # safe random function with help from:
    # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
    def get_random(table):
        max_id = table.objects.all().aggregate(max_id=Max("id"))['max_id']
        if max_id is None:
            return None
        while True:
            pk = random.randint(1, max_id)
            rand = table.objects.filter(pk=pk).first()
            if rand:
                return rand

    GAME_COUNT = 10
    games = []
    for i in range(GAME_COUNT):
        rand_game = get_random(Product)
        if rand_game is None:
            break

        games.append(rand_game)

    EVENT_COUNT = 10
    events = []
    for i in range(EVENT_COUNT):
        rand_ev = get_random(Events)
        if rand_ev is None:
            break

        desc = rand_ev.description
        # taken from: https://stackoverflow.com/a/2873416
        rand_ev.short_desc = desc[:100] + (desc[100:] and '...')

        events.append(rand_ev)

    context = {
        'random_games': games,
        'random_events': events
    }

    return render(request, 'home/index.html', context)
