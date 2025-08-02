import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# get all books by an author
author_name = input("Enter author name: ")
try:
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    books_by_author = Book.objects.filter(author=author) 
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"No author found with the name {author_name}")

# get all books in a library
library_name = input("Enter library name: ")
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")

# get librarian for a library
librarian = Librarian.objects.get(library='')
print(f"Librarian for {library.name}: {librarian.name}")
