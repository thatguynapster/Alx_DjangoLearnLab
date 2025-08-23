from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    # posts
    path("posts/", views.PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    # comments
    path(
        # "post/<int:post_id>/comments/new/",
        "post/<int:pk>/comments/new/",
        views.CommentCreateView.as_view(),
        name="comment_add",
    ),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment_edit",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    # Search
    path("search/", views.search_posts, name="search_posts"),
    # Tag-filtered posts
    path("tags/<slug:tag_slug>/", views.posts_by_tag, name="posts_by_tag"),
]
