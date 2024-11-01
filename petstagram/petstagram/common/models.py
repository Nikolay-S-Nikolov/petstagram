from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import PetPhoto

UserModel = get_user_model()


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )



# photo_like = PhotoLike.objects.filter(pet_photo_id=pet_photo.pk, user=request.user)
