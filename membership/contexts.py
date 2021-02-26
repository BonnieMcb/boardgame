from .models import Membership
from datetime import datetime


def get_membership(request):
    membership = None
    try:
        membership = Membership.objects.get(user=request.user)
    except (Membership.DoesNotExist, TypeError) as e:
        print("Membership not available for user: ", e)

    return membership


def is_membership_valid(request):
    membership = get_membership(request)
    if not membership:
        return False

    current_date = datetime.now().date()
    return current_date < membership.expiry
