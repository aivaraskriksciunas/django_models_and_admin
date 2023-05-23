from django.urls import path
from songs.views import show_song

urlpatterns = [
    path( "daina/", show_song )
]