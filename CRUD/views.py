from django.shortcuts import render, redirect
# Method 1: Directly importing using the model name
from .models import Products
# Method 2: Importing via models file
from . import models


# Create your views here.
def create(request):
    # Method 2: calling the data from models file
    # Creating a new instance of product form
    form = models.ProductsForm()
    # Checking the data inside POST method
    if request.method == 'POST':
        # Assigning a variable to the data that comes in form
        data = models.ProductsForm(request.POST)
        if data.is_valid():
            # if it is valid, save it to the database.
            data.save()
            return redirect('crud')
    context = {
        'form_html': form
    }
    return render(request, 'create.html', context)


def update(request):
    context = {}
    return render(request, 'update.html', context)


def delete(request):
    context = {}
    return render(request, 'delete.html', context)


def read(request):
    # Method 1: calling the products table directly from the models file
    products_data = Products.objects.all()
    context = {
        'html_data': products_data,
    }
    return render(request, 'read.html', context)
