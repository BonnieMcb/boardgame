from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There doesn't seem to be anyhing in your bag right now")
        return redirect(reverse('games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)

# pk_test_51IK7S8Hnux12jyTLfrxMKKSARKeSGXTKtZcTKSSveFCyKkgFABaBmzZnOdbj2Z39FJguEJdC1uQOR1ZdSNtEc3w700zLl8uXbt