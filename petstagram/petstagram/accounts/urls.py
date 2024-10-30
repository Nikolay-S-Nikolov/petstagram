from django.urls import path, include

from petstagram.accounts.views import SignupUser, \
    PetstagramLoginView, details_profile, edit_profile, delete_profile, signout_user

urlpatterns = (
    path("signup/", SignupUser.as_view(), name="signup_user"),
    path("signin/", PetstagramLoginView.as_view(), name="signin_user"),
    path("signout/", signout_user, name="signout_user"),
    path("profile/<int:pk>/", include([
        path("", details_profile, name="details_profile"),
        path("edit/", edit_profile, name="edit_profile"),
        path("delete/", delete_profile, name="delete_profile"),

    ])),
)
