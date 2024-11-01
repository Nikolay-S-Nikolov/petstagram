from django.urls import path

from petstagram.common.views import IndexView, like_pet_photo,add_comment

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pet_photo_like/<int:pk>/', like_pet_photo, name='like_pet_photo'),
    path('comment/<int:photo_id>/', add_comment, name='add_comment'),
)
