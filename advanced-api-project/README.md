# advanced-api-project — README

## Project overview

This project demonstrates an advanced Django REST Framework (DRF) API focused on custom serializers, generic views, and view-level customizations (hooks and permissions). The repository path for this work is `Alx_DjangoLearnLab/advanced-api-project`.

---

## Quick setup

### Install dependencies:

```bash
pip install django djangorestframework
```

---

## Serializers (`api/serializers.py`)

-   **BookSerializer** (ModelSerializer)

    -   Serializes `id`, `title`, `publication_year`, `author`.
    -   **Custom validation**: `validate_publication_year` ensures the year is not in the future.

-   **AuthorSerializer** (ModelSerializer)

    -   Serializes `id`, `name` and a nested `books` field using `BookSerializer(many=True, read_only=True)`.
    -   The nested `books` field is **read-only** in this implementation; see the Writable Nested section below for making it writable.

**Why nested and read-only?**

-   Nesting lets the API return an Author with its related Book list in one response. Setting `read_only=True` avoids accidental creation of `Book` instances when creating an `Author` unless you explicitly implement nested create/update logic.

---

## Views (api/views.py) — configuration & behavior

The project uses DRF generic views to separate concerns and keep code concise.

### Implemented views (Book)

-   `BookListView` — `generics.ListAPIView`

    -   Endpoint: `GET /books/`
    -   Purpose: Returns paginated list of books.
    -   Permissions: `AllowAny` (by default the project sets `IsAuthenticatedOrReadOnly` so unauthenticated users can read).

-   `BookDetailView` — `generics.RetrieveAPIView`

    -   Endpoint: `GET /books/<int:pk>/`
    -   Purpose: Return single book detail.
    -   Permissions: `AllowAny`

-   `BookCreateView` — `generics.CreateAPIView`

    -   Endpoint: `POST /books/create/`
    -   Purpose: Create a new book. Requires authentication.
    -   Permissions: `IsAuthenticated`
    -   **Custom hook**: `perform_create(self, serializer)` — used to control how the instance is saved (e.g., associate the book to request.user or add extra validation/side-effects before saving).

-   `BookUpdateView` — `generics.UpdateAPIView`

    -   Endpoint: `PUT /books/<int:pk>/update/` (or `PATCH`)
    -   Purpose: Update an existing book. Requires authentication.
    -   Permissions: `IsAuthenticated`
    -   **Custom hook**: `perform_update(self, serializer)` — place to add side-effects or custom save behavior.

-   `BookDeleteView` — `generics.DestroyAPIView`

    -   Endpoint: `DELETE /books/<int:pk>/delete/`
    -   Purpose: Delete a book. Requires authentication.
    -   Permissions: `IsAuthenticated`

### URL routing

Endpoints are declared in `api/urls.py` and included in the project `urls.py`. Example paths:

```txt
/books/                    -> BookListView
/books/<int:pk>/           -> BookDetailView
/books/create/             -> BookCreateView
/books/<int:pk>/update/    -> BookUpdateView
/books/<int:pk>/delete/    -> BookDeleteView
```

---
