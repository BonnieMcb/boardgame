from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from games.models import Product


# To render the bag contents page
def view_bag(request):
    return render(request, 'bag/bag.html')


def is_membership(prod_id):
    is_membership = False
    try:
        product = Product.objects.get(id=prod_id)
        is_membership = product.is_membership
    except (Product.DoesNotExist, TypeError) as e:
        print("Can't get product:", e)

    return is_membership


def handle_membership(request, bag):
    # ensure that only one membership can be added to bag simultaneously
    temp_bag = bag
    for bag_item_id in list(temp_bag.keys()):
        if is_membership(bag_item_id):
            del bag[bag_item_id]

    # get the membership
    membership_id = int(request.POST.get('membership_id'))

    # quantity is always 1 for memberships
    bag[membership_id] = 1


# To add specified quantity for specific product to the bag
def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if is_membership(item_id):
        handle_membership(request, bag)
        messages.success(request, 'Added membership to your bag')
    else:
        messages.success(request, 'Added item to your bag')
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


# To adjust the quantity of a specific product in the bag to specified amount
def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if is_membership(item_id):
        handle_membership(request, bag)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
