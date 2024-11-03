#Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949

```python
from bookshelf.models import Book

# Create a new Book 
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book_instance.save()

# Confirm successful creation
Book.objects.all().values()
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>