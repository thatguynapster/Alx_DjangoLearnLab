from .views import (
    # UserViewSet,
    RegisterView,
    LoginView,
    ProfileView,
    FollowUserView,
    UnfollowUserView,
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include


# router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow_user"),
    # path("", include(router.urls)),
]
