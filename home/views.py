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
        while True:
            pk = random.randint(1, max_id)
            rand = table.objects.filter(pk=pk).first()
            if rand:
                return rand

    GAME_COUNT = 10
    games = []
    for i in range(GAME_COUNT):
        games.append(get_random(Product))

    EVENT_COUNT = 10
    events = []
    for i in range(EVENT_COUNT):
        events.append(get_random(Events))

    context = {
        'random_games': games,
        'random_events': events
    }

    return render(request, 'home/index.html', context)
