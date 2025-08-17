# Django Blog Authentication System

This project implements a basic authentication system for a Django blog application. It includes user registration, login, logout, and profile management with secure handling of user credentials.

---

## Features

-   **User Registration**

    -   Users can create an account with a username, email, and password.
    -   Form validation ensures unique usernames and strong passwords.
    -   CSRF tokens included for security.

-   **User Login & Logout**

    -   Secure login using Django's built-in authentication system.
    -   Logout functionality ends the session securely.

-   **Profile Management**

    -   Authenticated users can view and update their profile.
    -   Users can update email and other details.
    -   Optional extension: add profile picture or bio via a custom profile model.

-   **Security**

    -   CSRF protection enabled on all forms.
    -   Passwords stored securely using Django's password hashing algorithms.
    -   Only authenticated users can access profile pages.

-   **Blog**
-   **_List View:_** Displays all blog posts with title and content snippet.
-   **_Detail View:_** Shows full post content.
-   **_Create View:_** Authenticated users can create posts.
-   **_Update View:_** Only the post's author can edit.
-   **_Delete View:_** Only the post's author can delete.
-   **Permissions:**
    -   Anyone can view posts.
    -   Only authenticated users can create posts.
    -   Only authors can update/delete their own posts.

---

## File Structure

django_blog/

-   blog/
-   -   templates/
-   -   -   blog/
-   -   -   -   base.html
-   -   -   -   register.html
-   -   -   -   home.html
-   -   -   -   login.html
-   -   -   -   profile.html
-   -   -   -   post_list.html
-   -   -   -   post_detail.html
-   -   -   -   post_form.html
-   -   -   -   post_confirm_delete.html
-   -   forms.py
-   -   views.py
-   -   urls.py
-   django_blog/
-   -   settings.py
-   -   urls.py

---

## Authentication Workflow

1. **Registration**

    - User visits `/register/`
    - Completes the signup form.
    - User account created and stored in the database.

2. **Login**

    - User visits `/login/`
    - Authenticates with username and password.
    - Session created on successful login.

3. **Logout**

    - User visits `/logout/`
    - Session cleared, user redirected to login.

4. **Profile**
    - Authenticated user visits `/profile/`
    - Can view and edit personal details.
    - Form submission updates user model.

---

## How to Test the Authentication System

1. **Registration**

    - Navigate to `http://127.0.0.1:8000/register/`
    - Fill out form and submit.
    - Confirm user is created in the database.

2. **Login**

    - Navigate to `http://127.0.0.1:8000/login/`
    - Enter valid credentials.
    - Confirm user is redirected to profile.

3. **Logout**

    - Navigate to `http://127.0.0.1:8000/logout/`
    - Confirm session ends and login is required again.

4. **Profile Management**
    - Navigate to `http://127.0.0.1:8000/profile/`
    - Update email or other details.
    - Confirm changes are saved in the database.

---

## How to Test CRUD for Posts

1. **List Posts**

-   Navigate to `http://127.0.0.1:8000/posts/`
-   You'll see all posts displayed with title and snippet.

2. **View Post Detail**

-   Click a post title in the list.

-   Or directly visit:

```python
http://127.0.0.1:8000/posts/<post_id>/
```

3. **Create a New Post**

-   Log in via the admin or Django login page.

-   Visit: http://127.0.0.1:8000/posts/new/

-   Fill in title and content, then submit.

4. **Update/Edit a Post**

-   Must be logged in as the post's author.

-   Visit:

```python
- http://127.0.0.1:8000/posts/<post_id>/edit/
```

5. **Delete a Post**

Must be logged in as the post's author.

Visit:

http://127.0.0.1:8000/posts/<post_id>/delete/

-   Confirm deletion on the form.

## 🔒 Permissions Summary

-   View/List/Detail: Public (no login required).

-   Create: Authenticated users only.

-   Edit/Delete: Only post's author.

## 📌 Notes

-   The author of a post is automatically set to the currently logged-in user.

-   CSRF protection is enabled on all forms.

-   Templates extend from base.html for consistent styling.

---

## Security Checklist

-   ✅ CSRF tokens on all forms.
-   ✅ Passwords hashed using Django's built-in password hasher.
-   ✅ Restricted access: profile view requires authentication.
-   ✅ Django's authentication backends ensure secure login.

---

## Requirements

-   Python 3.x
-   Django 5.x (or latest stable)
-   SQLite (default) or PostgreSQL/MySQL

Install dependencies:

```bash
pip install -r requirements.txt
```
