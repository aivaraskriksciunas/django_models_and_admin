import datetime

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