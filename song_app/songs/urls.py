from django.urls import path
from songs.views import show_song, AllSongView
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
]