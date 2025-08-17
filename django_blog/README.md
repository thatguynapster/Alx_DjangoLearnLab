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

---

## File Structure

django_blog/

-   blog/
-   -   templates/
-   -   -   blog/
-   -   -   -   register.html
-   -   -   -   login.html
-   -   -   -   profile.html
-   -   -   base.html
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
