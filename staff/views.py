from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .contexts import shop_list, is_staff, event_list, handle_url_params
from games.models import Product
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
            except (Events.DoesNotExist, TypeError) as e:
                print("Can't find event: ", e)

    messages.success(request, 'Event deleted')
    return redirect(reverse('event_list'))
