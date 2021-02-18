from django.shortcuts import render

from .models import Membership

# Create your views here.


def membership(request):

    context = dict()
    context["user"] = request.user

    user_membership = Membership.objects.get(user=request.user)
    if user_membership:
        context["expiry"] = user_membership.expiry

    return render(request, 'membership/membership.html', context)
