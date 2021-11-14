from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'app/index.html')


def content_1(request):
    return render(request, 'app/content_1.html')


def content_2(request):
    return render(request, 'app/content_2.html')


def content_3(request):
    return render(request, 'app/content_3.html')

def content_4(request):
    return render(request, 'app/content_4.html')

def photos(request):
    return render(request, 'app/photos.html')