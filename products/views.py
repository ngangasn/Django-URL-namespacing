from django.shortcuts import render, get_object_or_404

from .models import Product


def products(request):
    # fetch all the products in the database
    context = {'products': Product.objects.all()}
    template_name = 'products/list.html'
    return render(request, template_name, context)


def product(request, id):
    # fetch a single product with an id
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    template_name = 'products/detail.html'
    return render(request, template_name, context)
