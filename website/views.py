from django.shortcuts import render
from . import models


def index_page(request):
    if request.method == 'POST':
        vu_id = request.POST.get('tu_id')
        vu_name = request.POST.get('tu_name')
        vu_email = request.POST.get('tu_email')
        vu_contact = request.POST.get('tu_contact')
        us = models.User(u_id=vu_id, u_name=vu_name, u_email=vu_email, u_contact=vu_contact)
        if us is not None:
            us.save()
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')


def services_off(request):
    data = models.Services.objects.all()
    context = {'data': data}
    return render(request, 'services.html', context)


def login_page(request):
    return render(request, 'login_page.html')


def contact_us(request):
    return render(request, 'contact.html')
