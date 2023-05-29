import datetime

from django.http import HttpResponse
from django.shortcuts import render
from songs.models import Song
from authors.models import Author

# Create your views here.
def show_song( request ):
    all_songs = Song.objects.all()
    song = all_songs[0]

    return render(
        request,
        'songs/index.html',
        {
            'daina': song
        }
    )

def show_all_songs( request ):
    visos_dainos = Song.objects.all()
    # Select * FROM Songs
    # visos_dainos = [ ... ]
    pirma_daina = visos_dainos[0] # Song tipas
    # Jei DB nera dainu - mes klaida!

    return render(
        request,
        'songs/list.html',
        {
            'daina': pirma_daina
        }
    )

def create_song( request ):
#/songs/new/?title=manodaina&duration=250
    title = request.GET.get( 'title' )
    duration = request.GET.get( 'duration' )

    song = Song()
    song.title = title
    song.duration = duration
    song.genre = "Rock"
    song.release_date = datetime.datetime.now()
    song.author = Author.objects.first()
    song.save()

    return HttpResponse( f"Song created: {title}" )