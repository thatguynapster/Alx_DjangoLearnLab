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

## Endpoints

### Posts

#### List Posts

-   **URL:** `/api/posts/`
-   **Method:** GET
-   **Description:** Retrieve a paginated list of posts.
-   **Parameters (Optional):**
    -   `search`: Search posts by title or content.
-   **Response Example:**

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"author": "username",
			"title": "My First Post",
			"content": "This is the content of the first post.",
			"created_at": "2025-08-24T10:00:00Z",
			"updated_at": "2025-08-24T10:00:00Z"
		}
	]
}
```

#### Create Post

-   **URL:** `/api/posts/`
-   **Method:** POST
-   **Description:** Create a new post.
-   **Request Example:**

```json
{
	"title": "New Post Title",
	"content": "This is the content of the new post."
}
```

-   **Response Example:**

```json
{
	"id": 2,
	"author": "username",
	"title": "New Post Title",
	"content": "This is the content of the new post.",
	"created_at": "2025-08-24T11:00:00Z",
	"updated_at": "2025-08-24T11:00:00Z"
}
```

#### Retrieve Post

-   **URL:** `/api/posts/{id}/`
-   **Method:** GET
-   **Description:** Retrieve details of a specific post.

#### Update Post

-   **URL:** `/api/posts/{id}/`
-   **Method:** PUT/PATCH
-   **Description:** Update the post (only if the user is the author).

#### Delete Post

-   **URL:** `/api/posts/{id}/`
-   **Method:** DELETE
-   **Description:** Delete the post (only if the user is the author).

---

### Comments

#### List Comments

-   **URL:** `/api/comments/`
-   **Method:** GET
-   **Description:** Retrieve a paginated list of comments.
-   **Response Example:**

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"post": 1,
			"author": "username",
			"content": "This is a comment.",
			"created_at": "2025-08-24T10:30:00Z",
			"updated_at": "2025-08-24T10:30:00Z"
		}
	]
}
```

#### Create Comment

-   **URL:** `/api/comments/`
-   **Method:** POST
-   **Description:** Add a new comment to a post.
-   **Request Example:**

```json
{
	"post": 1,
	"content": "This is a comment."
}
```

-   **Response Example:**

```json
{
	"id": 2,
	"post": 1,
	"author": "username",
	"content": "This is a comment.",
	"created_at": "2025-08-24T11:30:00Z",
	"updated_at": "2025-08-24T11:30:00Z"
}
```

#### Retrieve Comment

-   **URL:** `/api/comments/{id}/`
-   **Method:** GET
-   **Description:** Retrieve details of a specific comment.

#### Update Comment

-   **URL:** `/api/comments/{id}/`
-   **Method:** PUT/PATCH
-   **Description:** Update the comment (only if the user is the author).

#### Delete Comment

-   **URL:** `/api/comments/{id}/`
-   **Method:** DELETE
-   **Description:** Delete the comment (only if the user is the author).

---

## Model Changes

### `User` Model (accounts/models.py)

-   Added a `following` field:
    ```python
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)
    ```

This allows users to follow other users without requiring reciprocity (one-way relationship).

## API Endpoints

### User Follow Management (accounts app)

| Endpoint                            | Method | Description     |
| ----------------------------------- | ------ | --------------- |
| `/accounts/follow/<int:user_id>/`   | POST   | Follow a user   |
| `/accounts/unfollow/<int:user_id>/` | POST   | Unfollow a user |

#### Example Request (Follow a User)

```http
POST /accounts/follow/2/
Authorization: Token <your_token>
```

#### Example Response

```json
{ "detail": "You are now following johndoe" }
```

---

### Feed Endpoint (posts app)

| Endpoint       | Method | Description                        |
| -------------- | ------ | ---------------------------------- |
| `/posts/feed/` | GET    | Retrieve posts from followed users |

#### Example Request

```http
GET /posts/feed/
Authorization: Token <your_token>
```

#### Example Response

```json
[
	{
		"id": 1,
		"author": "johndoe",
		"content": "My first post!",
		"created_at": "2025-08-24T15:45:00Z"
	},
	{
		"id": 2,
		"author": "janedoe",
		"content": "Another great day!",
		"created_at": "2025-08-24T16:10:00Z"
	}
]
```

---

## Likes and Notifications

### Overview

Added the ability for users to like posts and receive notifications when their posts are liked. It extends the social features of the platform by increasing interactivity and user engagement.

## Features Implemented

1.  **Likes on Posts:**
    -   Users can like/unlike posts.
    -   A post can display the total number of likes it has received.
2.  **Notifications System:**
    -   When a post is liked, the owner of the post receives a
        notification.
    -   Notifications are linked to users and can be marked as
        read/unread.
3.  **Endpoints Added:**
    -   `POST /api/posts/<int:post_id>/like/` → Like a post.
    -   `POST /api/posts/<int:post_id>/unlike/` → Unlike a post.
    -   `GET /api/notifications/` → Retrieve all notifications for the
        logged-in user.

## Summary of Changes

1. **User Model Updated**: Added `following` ManyToMany field.
2. **New Views**:
    - `FollowUserView`
    - `UnfollowUserView`
    - `FeedView`
3. **URLs Added**:
    - `/accounts/follow/<user_id>/`
    - `/accounts/unfollow/<user_id>/`
    - `/posts/feed/`

---
