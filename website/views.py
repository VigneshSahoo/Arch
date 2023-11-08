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
    if request.method == "POST":
        name = request.POST.get('so_name')
        desc = request.POST.get('so_description')
        price = request.POST.get('so_price')
        x = models.Services(s_name=name,
                            s_description=desc,
                            s_price=price)
        if x is not None:
            x.save()
            return render(request, 'services.html', context)
    else:
        return render(request, 'services.html', context)


def login_page(request):
    return render(request, 'login_page.html')


def contact_us(request):
    return render(request, 'contact.html')
