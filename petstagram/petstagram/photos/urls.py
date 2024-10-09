from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailView, edit_photo

urlpatterns = (
    path("add/", PetPhotoCreateView.as_view(), name="create photo"),
    path("<int:pk>/", include([
        path("", PetPhotoDetailView.as_view(), name="details photo"),
        path("edit/", edit_photo, name="edit photo"),
    ])),
)
