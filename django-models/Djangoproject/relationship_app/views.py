from django.shortcuts import render

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
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful registration

    def form_valid(self, form):
        # Automatically log the user in after successful registration
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
# Create your views here.
