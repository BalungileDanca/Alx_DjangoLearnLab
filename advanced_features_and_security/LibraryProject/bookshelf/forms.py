from django import forms
from .models import Book  # Import the model you want the form for

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # The model this form is based on
        fields = ['title', 'author', 'published_date', 'description']  # List the fields you want in the form