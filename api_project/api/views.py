from django.shortcuts import render
from rest_framework import generics
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,IsAdminUser ]

# Create your views here.
