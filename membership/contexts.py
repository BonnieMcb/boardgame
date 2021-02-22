from .models import Membership


def get_membership(request):
    membership = None
    try:
        membership = Membership.objects.get(user=request.user)
    except (Membership.DoesNotExist, TypeError) as e:
        print("Membership not available for user: ", e)

    return membership

