from django.shortcuts import render

# Create your views here.


def membership(request):
    return render(request, 'membership/membership.html')
