from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_view( request ):
    return HttpResponse( "Labas vakaras" )