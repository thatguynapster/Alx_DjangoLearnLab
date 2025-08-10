from django.urls import path
from .views import (
    AuthorListCreateView, AuthorDetailView,
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    # authors URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    
    # books URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]
