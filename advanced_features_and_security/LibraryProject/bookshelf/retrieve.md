#Retrieve and display all attributes of the book you just created.
```python
from bookshelf.models import Book
Book.objects.get(title="1984")

Book.objects.all().values()

<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

#