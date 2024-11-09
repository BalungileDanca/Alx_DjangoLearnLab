from django.urls import path
from .views import list_books, LibraryDetailView

urlpattern = [
    path('books', views=list_books, name='list_books'),
    path('library', view=LibraryDetailView.as_view, name='library_detail')
]