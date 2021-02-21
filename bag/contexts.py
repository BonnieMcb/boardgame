from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Product

from membership.models import Membership
from datetime import datetime
from decimal import *


def get_discount(request):
    user = request.user
    discount = 1.0

    try:
        user_membership = Membership.objects.get(user=user)
        current_date = datetime.now().date()
        if current_date < user_membership.expiry:
            # 10% for premium members
            if user_membership.is_premium:
                discount = 0.9
            # 5% for members
            else:
                discount = 0.95
    except (Membership.DoesNotExist, TypeError) as e:
        discount = 1.0

    return discount


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    total_discount = 0
    gross_total = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        # apply membership discounts, if needed
        unit_price = product.price

        discount = get_discount(request)
        if product.id < 5000:
            product.discounted_price = round(Decimal(discount * float(product.price)), 2)
            unit_price = product.discounted_price

        subtotal = quantity * unit_price
        gross_total += quantity * product.price

        total += subtotal
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal
        })

    grand_total = total
    total_discount = grand_total - gross_total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'gross_total': gross_total,
        'total_discount': total_discount
    }

    return context
