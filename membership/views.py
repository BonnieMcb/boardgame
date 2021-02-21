from django.shortcuts import render

from .models import Membership

# Create your views here.


def membership(request):

    context = dict()
    context["user"] = request.user

    try:
        user_membership = Membership.objects.get(user=request.user)
        context["expiry"] = user_membership.expiry
        context["is_premium"] = user_membership.is_premium
    except (Membership.DoesNotExist, TypeError) as e:
        context["expiry"] = None
        context["is_premium"] = None

    return render(request, 'membership/membership.html', context)
