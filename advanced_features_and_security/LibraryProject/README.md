
# Book Management System

This is a Django-based Book Management System that includes functionality for creating, viewing, editing, and deleting books. 

## Permissions and Access Control

The system uses custom permissions to manage access to different actions on the `Book` model. These permissions are enforced at the view level to ensure that only authorized users can perform specific actions.

### Custom Permissions Defined on `Book` Model

The following custom permissions have been added to the `Book` model:

- **`can_view_book`**: Allows a user to view a book's details.
- **`can_create_book`**: Allows a user to create a new book in the system.
- **`can_edit_book`**: Allows a user to edit an existing book's details.
- **`can_delete_book`**: Allows a user to delete a book from the system.

These permissions are defined in the `Book` model's `Meta` class, and they are enforced through Django's `@permission_required` decorator in the views.

### Groups and Permissions

In this system, users are assigned to different groups, each with a specific set of permissions:

- **Viewers**: Users who can only view books.
  - Permissions: `can_view_book`
  
- **Editors**: Users who can view and edit books.
  - Permissions: `can_view_book`, `can_create_book`, `can_edit_book`

- **Admins**: Users who have full access to all actions (view, create, edit, delete books).
  - Permissions: `can_view_book`, `can_create_book`, `can_edit_book`, `can_delete_book`

### Assigning Permissions to Users

Permissions are assigned to groups using Django's Admin interface or programmatically. 

#### Example: Assigning Permissions via Django Admin

1. **Login to Django Admin**:
   - Go to `/admin` and log in as a superuser.
   
2. **Create Groups**:
   - Create groups such as **Viewers**, **Editors**, and **Admins**.
   
3. **Assign Permissions**:
   - Assign the appropriate permissions to each group:
     - Viewers: `can_view_book`
     - Editors: `can_view_book`, `can_create_book`, `can_edit_book`
     - Admins: `can_view_book`, `can_create_book`, `can_edit_book`, `can_delete_book`

4. **Assign Users to Groups**:
   - Assign users to the appropriate groups based on their role in the system.

#### Example: Assigning Permissions Programmatically

You can also assign permissions to users programmatically in the Django shell:

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Get or create the groups
viewers = Group.objects.get_or_create(name='Viewers')[0]
editors = Group.objects.get_or_create(name='Editors')[0]
admins = Group.objects.get_or_create(name='Admins')[0]

# Get the content type for the Book model
content_type = ContentType.objects.get_for_model(Book)

# Assign permissions to each group
can_view = Permission.objects.get(codename='can_view_book', content_type=content_type)
can_create = Permission.objects.get(codename='can_create_book', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit_book', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete_book', content_type=content_type)

# Assign permissions to groups
viewers.permissions.add(can_view)
editors.permissions.add(can_view, can_create, can_edit)
admins.permissions.add(can_view, can_create, can_edit, can_delete)

# Assign users to groups as needed
