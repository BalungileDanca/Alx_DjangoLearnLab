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


from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm  # Import the default UserCreationForm
 

class register(CreateView):
    form_class = UserCreationForm  # Using Django's default form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    