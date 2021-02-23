from django.shortcuts import render, redirect, reverse

from .contexts import shop_list, is_staff
from games.models import Product
from .forms import ProductForm


def staff(request):

    if not is_staff(request):
        return redirect('/')

    return render(request, 'staff/staff.html')


def add_product(request):

    return render(request, 'staff/add_product.html')


def product_list(request):

    context = {
        'page_obj': shop_list(request)
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
    except (Product.DoesNotExist, TypeError) as e:
        print("Can't find product: ", e)

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
            except (Product.DoesNotExist, TypeError) as e:
                print("Can't find product: ", e)

    return redirect(reverse('product_list'))
