from django.shortcuts import render

from .models import Membership
from membership.contexts import get_membership

# Create your views here.


def membership(request):

    membership = get_membership(request)

    context = {
        'user': request.user,
        'navbar': 'membership',
        'membership': membership
    }

    return render(request, 'membership/membership.html', context)
