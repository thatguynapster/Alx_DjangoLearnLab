from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    Serializes all fields in the Book model.
    Includes validation to ensure publication_year is not in the future.
    """
    
    author_name = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author','author_name']
        
    def validate_publication_year(self, value):
        """
        Validate that the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    Serializes all fields in the Author model.
    Includes a nested representation of related books.
    """
    books = BookSerializer(many=True, read_only=True) # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
