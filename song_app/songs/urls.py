from django.urls import path
from unicodedata import name

from songs.views import (
    show_song,
    AllSongView,
    calculator_view, paieska
)
from songs.views import show_all_songs
from songs.views import create_song

urlpatterns = [
    # http://127.0.0.1:8000/songs/
    path( "", AllSongView.as_view() ),
    # http://127.0.0.1:8000/songs/daina/
    path( "daina/", show_song ),
    # http://127.0.0.1:8000/songs/list/
    path( "list/", show_all_songs ),
    # http://127.0.0.1:8000/songs/new/
    path( "new/", create_song ),
    # http://127.0.0.1:8000/songs/calculator/
    path( "calculator/", calculator_view ),
    # http://127.0.0.1:8000/songs/search/
    path( "paieska/", paieska, name = "song_search" ),
]