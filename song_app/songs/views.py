import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
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

class AllSongView( ListView ):
    model = Song
    paginate_by = 2

def paieska( request ):
    search = request.GET.get( "paieska" )
    duration = request.GET.get( "duration" )
    # Atvejai, kai gausim klaidą (iš filter funkcijos):
    # /songs/search?paieska=&duration=
    # duration yra '' (tuščias string)

    # /songs/search?paieska=
    # duration yra None (neegzistuojanti reikšmė)

    # Patikrinam, ar duration nėra None, ir ar yra sudarytas iš skaičių
    if duration is None or duration.isnumeric() == False:
        duration = 0

    # Filtravimas:
    # songs = Song.objects.filter(
    #     title__icontains=search
    #     duration=duration
    # )
    # Gautas SQL:
    # SELECT * FROM songs WHERE title LIKE ... AND duration = ...

    # Q klasė leidžia kriterijus kombinuoti su OR
    songs = Song.objects.filter(
        Q( title__icontains = search ) |
        Q( duration = duration )
    )
    # Gautas SQL:
    # SELECT * FROM songs WHERE title LIKE ... OR duration = ...

    return render(
        request,
        "songs/search_results.html",
        { "songs": songs }
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


# Užduotėlė:
# Sukurti calculator view, kuris susumuotų du skaičius, pvz:
# http://localhost:8000/songs/calculator/?a=12&b=98
# Paduotus parametrus a ir b sudėtų ir išvestų jų sumą
# http://127.0.0.1:8000/songs/calculator/?a=1&b=2
def calculator_view( request ):
    a = request.GET.get( 'a' )
    b = request.GET.get( 'b' )

    if a == None or b == None:
        return HttpResponse( "Pateikėte blogus duomenis" )

    suma = int( a ) + int( b )
    return render(
        request,
        'calculator/result.html',
        { 'result': suma }
    )