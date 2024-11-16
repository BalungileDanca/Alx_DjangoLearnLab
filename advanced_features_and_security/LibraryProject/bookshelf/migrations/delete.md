# Deleting a Book Instance
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the book to be deleted

book.delete()#Delete the book
(1, {'bookshelf.Book': 1})

# expected output confirming the deletion
Book.objects.all()
<QuerySet []>

