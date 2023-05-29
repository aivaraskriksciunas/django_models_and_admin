from django.urls import path
from songs.views import show_song
from songs.views import show_all_songs
from songs.views import create_song

urlpatterns = [
    path( "daina/", show_song ),
    path( "list/", show_all_songs ),
    path( "new/", create_song ),
]