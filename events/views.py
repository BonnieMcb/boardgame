from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Events
from profiles.models import UserProfile
from membership.contexts import is_membership_valid


def events(request):
    """ A view to show all events """

    events = Events.objects.all()

    for event in events:
        event.sign_list = event.signed_up_users.all()

    user = request.user

    context = {
        'events': events,
        'user': user
    }
    return render(request, 'events/events.html', context)


def sign(request, event_id):

    redirect_url = request.POST.get('redirect_url')

    # get event
    try:
        event = Events.objects.get(id=event_id)

        # to stop AnonymousUser signing for events
        user_profile = None
        try:
            user_profile = UserProfile.objects.get(id=request.user.id)
        except UserProfile.DoesNotExist:
            messages.error(request, "Please create an account in order to sign up for events!")

        # to ensure members-only events require membership
        can_sign = True
        if event.member_only:
            can_sign = is_membership_valid(request)
            if not can_sign:
                messages.error(request, "Event is only for members. Become a member to attend!")

        if user_profile and can_sign:
            event.signed_up_users.add(user_profile)
            messages.success(request, 'Signed up for event. Check your emails for further details')

    except (Events.DoesNotExist, TypeError) as e:
        print("Event does not exist", e)

    return redirect(redirect_url)


def unsign(request, event_id):

    redirect_url = request.POST.get('redirect_url')

    # get event
    try:
        event = Events.objects.get(id=event_id)

        user_profile = None
        try:
            user_profile = UserProfile.objects.get(id=request.user.id)
        except UserProfile.DoesNotExist:
            messages.error(request, "Please create an account in order to unsign from events!")

        if user_profile:
            event.signed_up_users.remove(user_profile)
            messages.success(request, 'Unsigned from event. Check your emails for further details')

    except (Events.DoesNotExist, TypeError) as e:
        print("Event not found", e)

    return redirect(redirect_url)
