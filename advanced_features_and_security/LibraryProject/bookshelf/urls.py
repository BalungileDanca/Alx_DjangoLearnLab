from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),  # Map the URL to the view
    # other URL patterns...
]