from django.urls import path
from .views import list_books, LibraryDetailView

urlpattern = [
    path('list', list_books,'list_books'),
    path('library', LibraryDetailView.as_view, 'library_detail')
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login View
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout View
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    # Register View (custom registration view)
    path('register/', views.register.as_view(), name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    # URL for adding a new book
    path('add/', views.add_book, name='add_book'),

    # URL for editing an existing book (requires a book ID as parameter)
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),

    # URL for deleting an existing book (requires a book ID as parameter)
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]