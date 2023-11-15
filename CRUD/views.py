from django.shortcuts import render


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
    context = {}
    return render(request, 'read.html', context)
