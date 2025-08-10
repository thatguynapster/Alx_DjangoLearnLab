from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    Lists all authors or creates a new author.
    GET  /authors/  → list authors
    POST /authors/  → create author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single author.
    GET    /authors/<id>/
    PUT    /authors/<id>/
    PATCH  /authors/<id>/
    DELETE /authors/<id>/
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    """
    Lists all books or creates a new book.
    GET  /books/  → list books
    POST /books/  → create book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single book.
    GET    /books/<id>/
    PUT    /books/<id>/
    PATCH  /books/<id>/
    DELETE /books/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
