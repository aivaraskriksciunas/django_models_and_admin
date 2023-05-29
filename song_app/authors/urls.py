from django.urls import path
from authors.views import (
    hello_view,
    create_author,
    AllAuthorsListView,
)

urlpatterns = [
    path( "hello/", hello_view ),
    path( "new/", create_author ),
    path( "", AllAuthorsListView.as_view() )
]