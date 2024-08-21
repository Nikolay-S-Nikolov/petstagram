from django.urls import path, include

from petstagram.accounts.views import signup_user, \
    signin_user, details_profile, edit_profile, delete_profile, signout_user

urlpatterns = (
    path("signup/", signup_user, name="signup_user"),
    path("signin/", signin_user, name="signin_user"),
    path("signout/", signout_user, name="signout_user"),
    path("profile/<int:pk>/", include([
        path("", details_profile, name="details_profile"),
        path("edit/", edit_profile, name="edit_profile"),
        path("delete/", delete_profile, name="delete_profile"),

    ])),
)
