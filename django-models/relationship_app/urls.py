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
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # Logout View
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Register View (custom registration view)
    path('register/', views.RegisterView.as_view(), name='register'),
]