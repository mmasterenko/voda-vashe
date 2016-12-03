from django.shortcuts import render


def home(request):
    return render(request, 'voda/index.html')


def where(request):
    return render(request, 'voda/where.html')


def about(request):
    return render(request, 'voda/about.html')
