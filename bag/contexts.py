from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Product

from membership.models import Membership
from datetime import datetime
from decimal import *


def get_discount(request):
    user = request.user

    user_membership = Membership.objects.get(user=user)
    if user_membership:
        current_date = datetime.now().date()
        if current_date < user_membership.expiry:
            # 20% for premium members
            if user_membership.is_premium:
                return 0.8
            # 10% for members
            else:
                return 0.9

    return 1.0


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        # apply membership discounts, if needed
        discount = get_discount(request)
        if product.id < 5000:
            product.discounted_price = round(Decimal(discount * float(product.price)), 2)

        subtotal = quantity * (product.discounted_price or product.price)

        total += subtotal
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
