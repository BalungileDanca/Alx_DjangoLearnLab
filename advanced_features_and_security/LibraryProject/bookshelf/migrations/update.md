# Updating a Book Instance
```python
from bookshelf.models import Book

#Retrieve the last Book instance
book_instance = Book.objects.get(title="1984")

# performing update
book_instance.title = "Nineteen Eighty-Four"
book_instance.save()

# expected output
<QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>



