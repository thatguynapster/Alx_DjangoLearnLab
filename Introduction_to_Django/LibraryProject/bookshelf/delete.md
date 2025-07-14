### Delete the Book Instance

# Retrieve and delete the book

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion

Book.objects.all()

# Expected Output:

(1, {'bookshelf.Book': 1})
<QuerySet []>
