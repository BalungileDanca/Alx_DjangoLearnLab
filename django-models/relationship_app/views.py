from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all() 
    context = {
        'list_books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

from .models import Library
from django.views.generic.detail import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.objects.book.all()  
        return context
# Create your views here.
