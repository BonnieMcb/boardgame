from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile
from checkout.models import Order
from events.models import Events

from checkout.forms import OrderForm

from membership.contexts import get_membership


def update_address(request):
    redirect_url = request.POST.get('redirect_url')

    try:
        profile = UserProfile.objects.get(user=request.user)
        form = OrderForm(request.POST, instance=profile)
        form.save()
    except (UserProfile.DoesNotExist, TypeError, ValueError) as e:
        print("Address update failed: ", e)

    return redirect(redirect_url)


def profile(request):

    # To display the user's profile.
    profile = None
    try:
        profile = UserProfile.objects.get(user=request.user)
    except (UserProfile.DoesNotExist, TypeError) as e:
        print("User not found:", e)

    membership = get_membership(request)
    user = request.user

    # get address details for this user, if there are any
    address_form = None
    if profile:
        address_form = OrderForm(instance=profile)

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
        'events': events,
        'order_form': address_form
    }

    return render(request, template, context)
