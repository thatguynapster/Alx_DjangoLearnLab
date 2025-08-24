# Social Media API – User Authentication

This is the initial setup of a **Social Media API** built with Django and Django REST Framework (DRF)

---

## 🚀 Setup Process

1. **Create a Virtual Environment and Activate It**

python -m venv venv
source venv/bin/activate # Linux / Mac
venv\Scripts\activate # Windows

2. **Install Dependencies**

pip install django djangorestframework

3. **Run Migrations**

python manage.py makemigrations
python manage.py migrate

4. **Create a Superuser (optional, for admin access)**

python manage.py createsuperuser

5 **Start the Development Server**

python manage.py runserver

## 🔑 User Authentication

Authentication is handled using DRF Token Authentication.

1. **Register**

Endpoint: `POST /accounts/register/`

Request Body:

```json
{
	"username": "john_doe",
	"email": "john@example.com",
	"password": "securepassword123"
}
```

Response:

```json
{
	"user": {
		"username": "john_doe",
		"email": "john@example.com"
	},
	"token": "generated-auth-token",
	"message": "User registered"
}
```

2. **Login**

Endpoint: `POST /accounts/login/`

Request Body:

```json
{
	"username": "john_doe",
	"password": "securepassword123"
}
```

Response:

```json
{
	"token": "generated-auth-token",
	"message": "Login successful"
}
```

3. **Profile**

Endpoint: `GET /accounts/profile/`

Headers:
`Authorization: Token <generated-auth-token>`

Response:

```json
{
	"id": 1,
	"username": "john_doe",
	"email": "john@example.com",
	"bio": "",
	"profile_picture": null,
	"followers": []
}
```

## 👤 User Model Overview

The project uses a custom user model that extends Django's AbstractUser.

Additional fields:

`bio` – Short user description.

`profile_picture` – Uploadable image for profile picture.

`followers` – A Many-to-Many relationship allowing users to follow each other (symmetrical=False).
