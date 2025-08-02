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
