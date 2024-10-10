from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailView, PetPhotoEditView, PetPhotoDeleteView

urlpatterns = (
    path("add/", PetPhotoCreateView.as_view(), name="create photo"),
    path("<int:pk>/", include([
        path("", PetPhotoDetailView.as_view(), name="details photo"),
        path("edit/", PetPhotoEditView.as_view(), name="edit photo"),
        path("delete/", PetPhotoDeleteView.as_view(), name="delete photo"),
    ])),
)
