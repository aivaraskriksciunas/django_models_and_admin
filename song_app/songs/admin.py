from django.contrib import admin
from songs.models import Song

# Register your models here.
# Atvaizduoti dainas admin puslapyje
# Prideti visus laukelius (i saraso vaizdavima)
# Prideti filtravima pagal zanra
class SongAdmin( admin.ModelAdmin ):
    list_display = [
        'title',
        'duration',
        'genre',
        'release_date',
        'author'
    ]
    list_filter = [ 'genre' ]
    # Kai vykdysim paiešką, jis ieškos pagal visus
    # šitus laukelius vienu metu:
    search_fields = [
        'id',
        'title',
        # Paieška pagal related fields:
        # Ieškos pagal dainos autoriaus pavardę
        'author__last_name'
    ]

admin.site.register( Song, SongAdmin )