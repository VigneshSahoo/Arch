from django.shortcuts import render
from . import data_file


def index_page(request):
    context = {'intro': data_file.intro}
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about.html')


def services_off(request):
    context = {'services': data_file.services_offered}
    return render(request, 'services.html', context)


def login_page(request):
    return render(request, 'login_page.html')


def contact_us(request):
    return render(request, 'contact.html')
