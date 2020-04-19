from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


def home(request):
    return HttpResponse("Hello world")


def musicians(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'musicians.html', context)


def musician_info(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id)
    }
    return render(request, 'musician_info.html', context)
