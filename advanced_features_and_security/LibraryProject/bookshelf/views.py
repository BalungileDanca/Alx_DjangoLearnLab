from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        # Create a new book instance
        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )
        return redirect('book_list')  # Redirect to book list view
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('edit', book_id=book.id)

    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_list')


from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(title__icontains=query)  # Safely searching for books
    return render(request, 'book_list.html', {'books': books})

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def create_book(request):
    # View logic here
    return render(request, 'create_book.html')

from django.shortcuts import render, redirect
from .forms import BookForm

from django.shortcuts import render, redirect
from .forms import ExampleForm  # Add this import to reference the form

def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the book instance
            return redirect('book_list')  # Redirect after saving
    else:
        form = ExampleForm()  # Empty form for GET request

    return render(request, 'bookshelf/create_book.html', {'form': form})