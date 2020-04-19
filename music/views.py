from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician, Album, Song


def home(request):
    return HttpResponse("Hello world")


def musicians(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'musicians.html', context)


def musician_info(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id),
        'albums': Album.objects.filter(artist=musician_id)

    }
    return render(request, 'musician_info.html', context)


def album_info(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album=album_id)

    }
    return render(request, 'album_info.html', context)


def song_info(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id)

    }
    return render(request, 'song_info.html', context)
