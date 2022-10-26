from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def index(request):
    # fetch all the products in the database
    context = {'articles': BlogPost.objects.all()}
    template_name = 'list.html'
    return render(request, template_name, context)


def article(request, id):
    # fetch a single product with an id
    article = get_object_or_404(BlogPost, id=id)
    context = {'article': article}
    template_name = 'detail.html'
    return render(request, template_name, context)
