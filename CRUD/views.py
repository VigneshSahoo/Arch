from django.shortcuts import render
# Method 1: Directly importing using the model name
from .models import Products
# Method 2: Importing via models file
from . import models


# Create your views here.
def create(request):
    context = {}
    return render(request, 'create.html', context)


def update(request):
    context = {}
    return render(request, 'update.html', context)


def delete(request):
    context = {}
    return render(request, 'delete.html', context)


def read(request):
    # Method 2: calling the data from models file
    data = models.Products.objects.all()
    # Method 1: calling the products table directly from the models file
    products_data = Products.objects.all()
    context = {
        'html_data': products_data,
    }
    return render(request, 'read.html', context)
