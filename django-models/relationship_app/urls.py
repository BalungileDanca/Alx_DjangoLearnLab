from django.urls import path
from .views import list_books, LibraryDetailView

urlpattern = [
    path('list', list_books,'list_books'),
    path('library', LibraryDetailView.as_view, 'library_detail')
]