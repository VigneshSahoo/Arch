from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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
    context = {}
    return render(request, 'about.html', context)


@login_required(login_url='login_page')
def services_off(request):
    data = models.Services.objects.all()
    logic = {'data': data}
    if request.method == "POST":
        x = models.Services(
            s_name=request.POST.get('s_name'),
            s_description=request.POST.get('s_description'),
            s_price=request.POST.get('s_price')
        )
        if x is not None:
            x.save()
            return render(request, 'services.html', logic)
    else:
        return render(request, 'services.html', logic)


def service_details(request, id):
    data = models.Services.objects.get(id=id)
    context = {'data': data}
    if request.method == 'POST':

        data.s_name = request.POST.get('prodname')
        data.s_description = request.POST.get('desc')
        data.s_price = request.POST.get('price')

        data.save()
        return redirect('services')
    return render(request, 'service_detail.html', context)


def delete_service(request, pk):
    data = models.Services.objects.get(pk=pk)
    data.delete()
    return redirect('services')


def servicesform(request):
    data = models.ServicesForm()
    if request.method == 'POST':
        data = models.ServicesForm(request.POST)
        if data.is_valid():
            data.save()
    context = {'form': data}
    return render(request, 'subscribe.html', context)


def subscribe(request):
    data = models.SubscriptionForm()
    if request.method == 'POST':
        data = models.SubscriptionForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/')
    context = {'form': data}
    return render(request, 'subscribe.html', context)


def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
            )
        if user is not None:
            login(request, user=user)
            return redirect('services')
    return render(request, 'login_page.html')


def contact_us(request):
    return render(request, 'contact.html')


def crud(request):
    context = {}
    return render(request, 'crud.html', context)


def registration(request):
    forms = models.TotalUsers()
    if request.method == 'POST':
        user = models.TotalUsers(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login_page')
    context = {'form': forms}
    return render(request, 'registration.html', context)
