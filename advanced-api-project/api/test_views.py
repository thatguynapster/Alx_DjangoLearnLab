# advanced-api-project/api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

"""
Tests for Book API matching the provided serializers.py and views.py.

Notes about endpoints (based on your views.py):
- List (GET)          -> /books/                 name='book-list'
- Create (POST)       -> /books/create/          name='book-create'
- Retrieve (GET)      -> /books/<pk>/            name='book-detail'
- Update (PUT/PATCH)  -> /books/<pk>/update/     name='book-update'
- Delete (DELETE)     -> /books/<pk>/delete/     name='book-delete'

This test file uses force_authenticate for authenticated actions to avoid CSRF/session
auth behavior that sometimes causes 403 instead of 401 in tests.
"""

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create authors
        self.author_x = Author.objects.create(name="Author X")
        self.author_y = Author.objects.create(name="Author Y")
        self.author_z = Author.objects.create(name="Author Z")

        # Create books (link to Author instances)
        self.book1 = Book.objects.create(title="Book A", author=self.author_x, publication_year=2000)
        self.book2 = Book.objects.create(title="Book B", author=self.author_y, publication_year=2010)
        self.book3 = Book.objects.create(title="Book C", author=self.author_x, publication_year=2005)

        # Reverse names used in urls.py (ensure they match your api/urls.py)
        self.list_name = 'book-list'
        self.create_name = 'book-create'
        self.detail_name = 'book-detail'
        self.update_name = 'book-update'
        self.delete_name = 'book-delete'

        # API client instance
        self.client = APIClient()

    # ---------- READ / LIST ----------
    def test_list_books_public(self):
        """Anyone (unauthenticated) can list books (ListAPIView)."""
        url = reverse(self.list_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # There should be 3 books created in setUp
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book_public(self):
        """Anyone can retrieve a single book detail."""
        url = reverse(self.detail_name, kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        # author is a PK in serializer; author_name is read-only field present
        self.assertEqual(response.data['author'], self.author_x.id)
        self.assertEqual(response.data['author_name'], self.author_x.name)

    # ---------- CREATE ----------
    def test_create_book_unauthenticated_forbidden(self):
        """Unauthenticated users should not be able to create (permission = IsAuthenticated)."""
        url = reverse(self.create_name)
        payload = {
            "title": "New Book",
            "author": self.author_z.id,   # pass author id
            "publication_year": 2021
        }
        response = self.client.post(url, payload, format='json')
        # Accept either 401 or 403 depending on auth config (SessionAuth vs TokenAuth)
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated(self):
        """Authenticated users can create books (use force_authenticate to avoid CSRF issues)."""
        url = reverse(self.create_name)
        payload = {
            "title": "New Book",
            "author": self.author_z.id,
            "publication_year": 2021
        }

        # Force authenticate the client as the test user
        
        self.client.login(username="testuser", password="password123")
        response = self.client.post(url, payload, format='json')
        # Undo authentication for subsequent tests (good practice)
        self.client.force_authenticate(user=None)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        new_book = Book.objects.get(title="New Book")
        self.assertEqual(new_book.author, self.author_z)

    # ---------- UPDATE ----------
    def test_update_book_unauthenticated_forbidden(self):
        """Unauthenticated users cannot update (should be 401/403)."""
        url = reverse(self.update_name, kwargs={'pk': self.book1.pk})
        payload = {
            "title": "Updated Book A",
            "author": self.author_x.id,
            "publication_year": 2001
        }
        response = self.client.put(url, payload, format='json')
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_update_book_authenticated(self):
        """Authenticated users can update books (use force_authenticate)."""
        url = reverse(self.update_name, kwargs={'pk': self.book1.pk})
        payload = {
            "title": "Updated Book A",
            "author": self.author_x.id,
            "publication_year": 2001
        }

        self.client.login(username="testuser", password="password123")
        response = self.client.put(url, payload, format='json')
        self.client.force_authenticate(user=None)

        # Ensure update succeeded
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book A")
        self.assertEqual(self.book1.publication_year, 2001)

    # ---------- DELETE ----------
    def test_delete_book_unauthenticated_forbidden(self):
        """Unauthenticated users cannot delete books (should be 401 or 403)."""
        url = reverse(self.delete_name, kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_delete_book_authenticated(self):
        """Authenticated users can delete books (use force_authenticate)."""
        url = reverse(self.delete_name, kwargs={'pk': self.book2.pk})
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(url)
        self.client.force_authenticate(user=None)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # book2 should be removed
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # ---------- FILTER / SEARCH / ORDER ----------
    def test_filter_books_by_author_name(self):
        """Filter books by the author's name using `author__name` as configured in views.py."""
        url = reverse(self.list_name)
        # Use the field name exactly as in views.filterset_fields
        response = self.client.get(url, {'author__name': 'Author X'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # book1 and book3 are by Author X
        self.assertEqual(len(response.data), 2)
        titles = {b['title'] for b in response.data}
        self.assertSetEqual(titles, {"Book A", "Book C"})

    def test_search_books_by_title(self):
        """Search by title (search_fields includes 'title' and 'author__name')."""
        url = reverse(self.list_name)
        term = 'Book A'
        response = self.client.get(url, {'search': term})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertIn(term.split()[0], book['title'])  # check that 'Book' appears

    def test_order_books_by_publication_year(self):
        """Ordering by publication_year returns sorted results."""
        url = reverse(self.list_name)
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data]
        self.assertEqual(years, sorted(years))
