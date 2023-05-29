from django.contrib import admin
from authors.models import Author
from songs.models import Song

class SongInline( admin.TabularInline ):
    # Čia nustatome, kaip atsivaizduos dainos laukeliai
    # kai nueisime į autoriaus redagavimo puslapį

    # Pasakome, kad čia aprašysime būtent Song modelį
    model = Song    # Vienintelis privalomas nustatymas
    # Daug kitų pasirinktinų nustatymų iš dokumentacijos
    can_delete = False
    readonly_fields = [ 'duration', 'genre', 'release_date' ]

class AuthorAdmin( admin.ModelAdmin ):
    # Tai įjungia vaizdavima autoriui priklausančių dainų,
    # kai pasirenkam redaguoti vieną autorių
    # Django automatiškai žino, kad Song ir Author
    # yra susieti su ForeignKey
    inlines = [ SongInline ]

    # Nurodo, kokie laukeliai bus matomi Admin sarase
    list_display = [
        # Laukeliai paimami iš Author model
        'id',
        'first_name',
        'last_name',
        'birth_date',
        'linksmas_laukelis', # laukelio nėra DB, todėl jam sukūrėm funkciją
        'created_at',
        'updated_at',
    ]
    list_filter = [ 'id', 'first_name' ]
    # Laukelis iš dokumentacijos pavyzdžiui
    actions_on_bottom = True

    # Nurodo, kurie laukeliai (is Author modelio) atsiras
    # modifikavimo formoje
    # fields = [ 'first_name', 'birth_date' ]

    # Alternatyva fields:
    # leidžia suskirstyti formos elementus į sekcijas
    fieldsets = [
        [
            "Autoriaus vardas", # Sekcijos pavadinimas
            {
                # Laukeliai, esantys sekcijoje
                "fields": [ 'first_name', 'last_name' ]
            }
        ],
        [
            "Autoriaus duomenys",
            {
                "fields": [ 'birth_date' ]
            }
        ]
    ]

    # Iš list_display, čia apsirašom laukelį kurio nebuvo modelyje
    def linksmas_laukelis( self, model ):
        # model yra Author klases objektas
        song_list = []
        for song in model.song_set.all():
            song_list.append( song.title )

        str_song_list = ", ".join( song_list )

        str_song_list = ", ".join( song.title for song in model.song_set.all() )
        return f":D {str_song_list}"

# Register your models here.
admin.site.register( Author, AuthorAdmin )