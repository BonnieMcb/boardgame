from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from checkout.models import Order
from events.models import Events

from membership.contexts import get_membership

# Create your views here.


def profile(request):

    # To display the user's profile.
    profile = None
    try:
        profile = UserProfile.objects.get(user=request.user)
    except (UserProfile.DoesNotExist, TypeError) as e:
        print("User not found:", e)

    membership = get_membership(request)
    user = request.user


    # get previous orders by this user, if there are any
    orders = None
    try:
        orders = Order.objects.filter(username=request.user)
    except (Order.DoesNotExist, TypeError) as e:
        print("Can't get orders for user:", e)


    # get event signs for this user
    events = None
    try:
        events = Events.objects.filter(signed_up_users=profile)
        # count signees for each event
        for event in events:
            event.sign_count = event.signed_up_users.count()
    except (Events.DoesNotExist, TypeError) as e:
        print("Cannot find events for user:", e)


    template = 'profiles/profile.html'
    context = {
        'user': request.user,
        'profile': profile,
        'membership': membership,
        'orders': orders,
        'events': events
    }

    return render(request, template, context)
