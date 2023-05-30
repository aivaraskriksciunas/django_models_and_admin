import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from authors.models import Author

# Create your views here.
def hello_view( request ):
    all_authors = Author.objects.filter( first_name = "Stasys" ) # Grazina list
    # Select * FROM Authors WHERE first_name = "Stasys"
    all_authors = Author.objects.filter( first_name__startswith="S" )
    # Select * FROM Authors WHERE first_name LIKE "S%"
    author = all_authors[0] # Istraukiam 1a is listo

    return render(
        request,
        'authors/index.html',
        {
            'pasisveikinimas': 'Hello world!',
            'author': author,
        }
    )

"""
Sukurti puslapį, kuriame būtų galima sukurti autorių pagal paduotus parametrus 
(pvz /authors/new/?first_name=vardas&last_name=pavarde). 
Galit pasirinkti kuriuos parametrus norite leisti paduoti vartotojui, 
ir kuriuos įrašysite per kodą (hardcoded). Siųsdami užklausas sukurkite 10 autorių.
"""
def create_author( request ):
    # /authors/new/?first_name=Jonas&last_name=Jonaitis
    first_name = request.GET.get( "first_name" )
    last_name = request.GET.get( "last_name" )
    # Čia turėtų būti patikrinimas, ar žmogus įvedė gerus duomenis

    author = Author()
    author.first_name = first_name
    author.last_name = last_name
    author.birth_date = datetime.datetime.now()
    author.save()

    return HttpResponse( "Naujas autorius pridetas" )

class AllAuthorsListView( ListView ):
    model = Author
    paginate_by = 2


"""
Analogiškai kaip su songs, atlikti šiuos pakeitimus authors appse:
Sukurti paieškos formą pagal vardą, pavardę
Atvaizduoti paieškos rezultatus
Papildomai pridėti paiešką pagal gimimo datą (rodyti autorius gimusius vėliau pateiktos datos)
"""

def search( request ):
    vardas = request.GET.get( "first_name" )
    last_name = request.GET.get( "last_name" )
    birth_date = request.GET.get( "birth_date" )

    # Tikrinimas...

    authors = Author.objects.filter(
        ( Q( first_name__icontains = vardas ) |
          Q( last_name__icontains = last_name ) )
        & Q( birth_date__gte = birth_date )
    )
    # SELECT * FROM songs WHERE
    #   (first_name LIKE ... OR last_name LIKE ... ) AND
    #   birth_date >= ...

    return render(
        request,
        "authors/paieskos_rezultatai.html",
        { "authors": authors }
    )