from django.shortcuts import render
from songs.models import Song

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