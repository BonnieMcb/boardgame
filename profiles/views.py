from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Create your views here.


def profile(request):

    # To display the user's profile.
    profile = None
    try:
        profile = UserProfile.objects.get(user=request.user)
    except (UserProfile.DoesNotExist, TypeError) as e:
        print("User not found:", e)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
