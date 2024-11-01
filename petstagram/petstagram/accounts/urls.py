from django.urls import path, include

from petstagram.accounts.views import SignupUser, \
    PetstagramLoginView, PetstagramLogoutView, \
    ProfileEditView, ProfileDetailsView , ProfileDeleteView

urlpatterns = (
    path("signup/", SignupUser.as_view(), name="signup_user"),
    path("signin/", PetstagramLoginView.as_view(), name="signin_user"),
    path("signout/", PetstagramLogoutView.as_view(), name="signout_user"),
    path("profile/<int:pk>/", include([
        path("", ProfileDetailsView.as_view(), name="details_profile"),
        path("edit/", ProfileEditView.as_view(), name="edit_profile"),
        path("delete/", ProfileDeleteView.as_view(), name="delete_profile"),

    ])),
)
