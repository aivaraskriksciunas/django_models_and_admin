from django.http import HttpResponse
from django.shortcuts import render
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