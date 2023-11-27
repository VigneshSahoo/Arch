from django.shortcuts import render


# Create your views here.
def landing(request):
    context = {}
    return render(request, 'landing.html', context)


def content(request):
    context = {}
    return render(request, 'content.html', context)
