from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from games.models import Product
from membership.models import Membership
from bag.contexts import bag_contents

# for membership calculations
from dateutil.relativedelta import *
from datetime import datetime

import stripe
import json


# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There doesn't seem to be anyhing in your bag right now")
            return redirect(reverse('games'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

# pk_test_51IK7S8Hnux12jyTLfrxMKKSARKeSGXTKtZcTKSSveFCyKkgFABaBmzZnOdbj2Z39FJguEJdC1uQOR1ZdSNtEc3w700zLl8uXbt


def try_apply_purchased_membership(request, bag):

    MEMBERSHIP_MIN_ID = 5000

    # check if there was a membership in the bag
    for item_id in list(bag.keys()):
        item_id_int = int(item_id)
        if item_id_int >= MEMBERSHIP_MIN_ID:

            len = None
            is_premium = False

            # TODO: this code is purposefully simple to avoid adding a whole new payment concept
            if item_id_int == 5000:
                len = 1
            elif item_id_int == 5001:
                len = 6
            elif item_id_int == 5002:
                len = 12
            elif item_id_int == 5003:
                len = 1
                is_premium = True
            elif item_id_int == 5004:
                len = 6
                is_premium = True
            elif item_id_int == 5005:
                len = 12
                is_premium = True

            if len:

                expiry = datetime.now()

                # check for existing membership for this user
                member_obj = Membership.objects.get(user=request.user)

                # calculate end date
                if member_obj:
                    current_datetime = datetime.combine(member_obj.expiry, datetime.min.time())
                    if current_datetime > expiry:
                        expiry = current_datetime
                else:
                    member_obj = Membership(
                        user=request.user)

                member_obj.expiry = (expiry + relativedelta(months=+len)).date()
                member_obj.is_premium = is_premium

                # insert or update membership entry
                member_obj.save()


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        # check if we just redeemed any memberships, and apply them if we did
        bag = request.session['bag']
        try_apply_purchased_membership(request, bag)

        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
