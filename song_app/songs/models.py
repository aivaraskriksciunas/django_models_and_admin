from django.db import models
from authors.models import Author

# Create your models here.
# Song
# title - pavadinimas
# duration - ilgis (s) - int
# genre - zanras - charfield
# release_date - date

# created_at
# updated_at
class Song( models.Model ):
    title = models.CharField( max_length = 80 )
    duration = models.IntegerField()
    genre = models.CharField( max_length = 10 )
    release_date = models.DateField( help_text = "Song release date" )
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE
    )

    # Saugoti kada buvo sukurtas ar atnaujintas
    created_at = models.DateTimeField( auto_now_add=True )
    update_at = models.DateTimeField( auto_now=True )

