from django.urls import path
from .views import list_books, libraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', libraryDetailView.as_view(), name='library_detail'),
]