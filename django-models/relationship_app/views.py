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
from .forms import CustomUserCreationForm  # Custom form (optional)

class RegisterView(CreateView):
    form_class = UserCreationForm  # Using Django's built-in UserCreationForm
    template_name = 'registration/register.html'  # Path to your registration template
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration

    def form_valid(self, form):
        # Automatically log the user in after successful registration
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')