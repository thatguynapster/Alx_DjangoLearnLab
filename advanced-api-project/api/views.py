from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Book Views
## List all books (Read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Lists all books. Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve single book
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieve details of a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book. Only for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook: Validate and save the book.
        Could be extended to associate books with a specific user.
        """
        serializer.save()


# Update existing book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/update/<id>
    Updates an existing book. Only for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook: Validate and save updates.
        """
        serializer.save()


# Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/<id>
    Deletes a book. Only for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


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
