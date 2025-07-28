from .views import add_book, edit_book, delete_book, admin_view, librarian_view, member_view, register_view, list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]