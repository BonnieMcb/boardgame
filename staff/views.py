from django.shortcuts import render, redirect, reverse
from django.contrib import messages

import string
from .contexts import shop_list, is_staff, event_list, handle_url_params
from games.models import Product, Category, Mechanic
from events.models import Events
from .forms import ProductForm, EventForm


def staff(request):

    if not is_staff(request):
        return redirect('/')

    return render(request, 'staff/staff.html')
    

def add_product(request):

    form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'staff/add_product.html', context)


def product_list(request):

    url_params = handle_url_params(request)

    context = {
        'page_obj': shop_list(request),
        'get_params': url_params
    }

    return render(request, 'staff/product_list.html', context)


def edit_product(request, product_id):

    form = None
    try:
        prod = Product.objects.get(id=product_id)
        form = ProductForm(instance=prod)
    except (Product.DoesNotExist, TypeError) as e:
        print("Can't find product: ", e)

    context = {
        'form': form,
        'product_id': product_id
    }

    return render(request, 'staff/edit_product.html', context)


def commit_edit(request, prod_id):

    redirect_url = request.POST.get('redirect_url')

    try:
        prod = Product.objects.get(id=prod_id)
        form = ProductForm(request.POST, instance=prod)
        form.save()
        messages.success(request, 'Product edited')
    except (Product.DoesNotExist, TypeError) as e:
        print("Can't find product: ", e)

    return redirect(redirect_url)


def commit_add(request):

    redirect_url = request.POST.get('redirect_url')

    form = ProductForm(request.POST)
    form.save()

    messages.success(request, 'Product added')

    return redirect(redirect_url)


def remove_product(request):

    post_data = request.POST.get('product_ids')
    if post_data:
        product_ids = post_data.split(',')
        for product_id in product_ids:
            # get the game
            try:
                prod = Product.objects.get(id=product_id)
                # remove the game
                prod.delete()
                messages.success(request, 'Product deleted')
            except (Product.DoesNotExist, TypeError) as e:
                print("Can't find product: ", e)

    return redirect(reverse('product_list'))


""" Views for Events are below """


def add_event(request):

    form = EventForm()

    context = {
        'form': form
    }

    return render(request, 'staff/add_event.html', context)


def events_list(request):

    url_params = handle_url_params(request)

    context = {
        'page_obj': event_list(request),
        'get_params': url_params
    }
    return render(request, 'staff/event_list.html', context)


def edit_event(request, event_id):

    form = None
    try:
        event = Events.objects.get(id=event_id)
        form = EventForm(instance=event)
    except (Events.DoesNotExist, TypeError) as e:
        print("Can't find event: ", e)

    context = {
        'form': form,
        'event_id': event_id
    }

    return render(request, 'staff/edit_event.html', context)


def commit_edit_event(request, event_id):

    redirect_url = request.POST.get('redirect_url')

    try:
        event = Events.objects.get(id=event_id)
        form = EventForm(request.POST, instance=event)
        form.save()
        messages.success(request, 'Event edited')
    except (Events.DoesNotExist, TypeError) as e:
        print("Can't find event: ", e)

    return redirect(redirect_url)


def commit_add_event(request):

    redirect_url = request.POST.get('redirect_url')

    try:
        form = EventForm(request.POST)
        form.save()
        messages.success(request, 'Event added')
    except ValueError as e:
        print("VE", e)

    return redirect(redirect_url)


def remove_event(request):

    post_data = request.POST.get('event_ids')
    if post_data:
        event_ids = post_data.split(',')
        for event_id in event_ids:
            # get the event
            try:
                event = Events.objects.get(id=event_id)
                # remove the event
                event.delete()
                messages.success(request, 'Event deleted')
            except (Events.DoesNotExist, TypeError) as e:
                print("Can't find event: ", e)

    return redirect(reverse('event_list'))


def category_list(request):

    all_cats = Category.objects.all()

    context = {
        'categories': all_cats
    }

    return render(request, 'staff/category_list.html', context)


# code from data_convert.py
def get_safe_name(friendly_name):
    # transform contents into db-friendly name
    # code modified from medium.com @ shorturl.at/eCQ02
    text_string = friendly_name.translate(str.maketrans(
        '', '', string.punctuation))
    safename = text_string.translate(str.maketrans(
        '', '', string.whitespace)).lower()
    return safename


def category_edit(request):

    redirect_url = request.POST.get('redirect_url')

    if 'name' in request.POST and 'id' in request.POST:
        try:
            cat = Category.objects.get(id=request.POST.get('id'))
            friendly_name = request.POST.get('name')
            name = get_safe_name(friendly_name)
            # set new values and save
            cat.friendly_name = friendly_name
            cat.name = name
            cat.save()
            messages.success(request, 'Categories edited')
        except (Category.DoesNotExist, ValueError) as e:
            print("Cannot find category", e)

    return redirect(redirect_url)


def category_add(request):

    redirect_url = request.POST.get('redirect_url')

    if 'name' in request.POST:
        friendly_name = request.POST.get('name')
        name = get_safe_name(friendly_name)
        cat = Category(name=name, friendly_name=friendly_name)
        cat.save()
        messages.success(request, 'Category added')

    return redirect(redirect_url)


def category_remove(request):

    post_data = request.POST.get('cat_ids')
    if post_data:
        cat_ids = post_data.split(',')
        for cat_id in cat_ids:
            # get the event
            try:
                category = Category.objects.get(id=cat_id)
                # remove the category
                category.delete()
                messages.success(request, 'Category deleted')
            except (Category.DoesNotExist, TypeError) as e:
                print("Can't find category: ", e)

    return redirect(reverse('categories'))


def mechanic_list(request):

    all_mechs = Mechanic.objects.all()

    context = {
        'mechanics': all_mechs
    }

    return render(request, 'staff/mechanic_list.html', context)


def mechanic_edit(request):

    redirect_url = request.POST.get('redirect_url')

    if 'name' in request.POST and 'id' in request.POST:
        try:
            mech = Mechanic.objects.get(id=request.POST.get('id'))
            friendly_name = request.POST.get('name')
            name = get_safe_name(friendly_name)
            # set new values and save
            mech.friendly_name = friendly_name
            mech.name = name
            mech.save()
            messages.success(request, 'Mechanics edited')
        except (Mechanic.DoesNotExist, ValueError) as e:
            print("Cannot find mechanic", e)

    return redirect(redirect_url)


def mechanic_add(request):

    redirect_url = request.POST.get('redirect_url')

    if 'name' in request.POST:
        friendly_name = request.POST.get('name')
        name = get_safe_name(friendly_name)
        mech = Mechanic(name=name, friendly_name=friendly_name)
        mech.save()
        messages.success(request, 'Mechanic added')

    return redirect(redirect_url)


def mechanic_remove(request):

    post_data = request.POST.get('mech_ids')
    if post_data:
        mech_ids = post_data.split(',')
        for mech_id in mech_ids:
            # get the event
            try:
                mech = Mechanic.objects.get(id=mech_id)
                # remove the mechanic
                mech.delete()
                messages.success(request, 'Mechanic deleted')
            except (Mechanic.DoesNotExist, TypeError) as e:
                print("Can't find mechanic: ", e)

    return redirect(reverse('mechanics'))
