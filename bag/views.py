from django.shortcuts import render, redirect, reverse, HttpResponse

MEMBERSHIP_ID_MIN = 5000


# To render the bag contents page
def view_bag(request):
    return render(request, 'bag/bag.html')


def handle_membership(request, bag):
    # ensure that only one membership can be added to bag simultaneously
    temp_bag = bag
    for bag_item_id in list(temp_bag.keys()):
        bag_item_id_int = int(bag_item_id)
        if bag_item_id_int >= MEMBERSHIP_ID_MIN:
            del bag[bag_item_id]

    # get the membership
    membership_id = int(request.POST.get('membership_id'))

    # quantity is always 1 for memberships
    bag[membership_id] = 1


# To add specified quantity for specific product to the bag
def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    item_id_int = int(item_id)
    if item_id_int >= MEMBERSHIP_ID_MIN:
        handle_membership(request, bag)
    else:
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

    item_id_int = int(item_id)
    if item_id_int >= MEMBERSHIP_ID_MIN:
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
