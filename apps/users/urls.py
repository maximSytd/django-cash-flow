from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "signup/",
        views.SignUpView.as_view(),
        name="signup",
    ),
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "profile/",
        views.ProfileView.as_view(),
        name="profile",
    ),
    path(
        "update-initials/",
        views.UserInitialsUpdateView.as_view(),
        name="update_initials",
    ),
    path(
        "update-avatar/",
        views.UserAvatarUpdateView.as_view(),
        name="update_avatar",
    ),
]