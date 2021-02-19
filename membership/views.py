from django.shortcuts import render

from .models import Membership

# Create your views here.


def membership(request):

    context = dict()
    context["user"] = request.user

    try:
        user_membership = Membership.objects.get(user=request.user)
        context["expiry"] = user_membership.expiry
    except (Membership.DoesNotExist, TypeError) as e:
        context["expiry"] = None

    return render(request, 'membership/membership.html', context)
