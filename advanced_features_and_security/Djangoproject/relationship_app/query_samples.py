from relationship_app.models import Book, Author, Library, Librarian

def books_by_author(author):
    try:
        books = Book.objects.filter(author=author)
        books = author.books.all()  
        print(f"Books by {author}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"No author found with the name {author}")


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")


def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")