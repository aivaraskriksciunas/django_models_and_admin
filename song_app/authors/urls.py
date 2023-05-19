from django.urls import path
from authors.views import hello_view

urlpatterns = [
    path( "hello/", hello_view )
]