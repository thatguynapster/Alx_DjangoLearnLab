# Create a Book instance

```
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

# Output the created object

```
book
```

# Expected output

<Book: Book object (1)>

### Update the book details

# Get the book instance

book = Book.objects.get(title="1984")

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

# Confirm updated title

book.title

# Expected output

'Nineteen Eighty-Four'

### Delete the Book Instance

# Retrieve and delete the book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion

Book.objects.all()

# Expected Output:

(1, {'bookshelf.Book': 1})
<QuerySet []>
