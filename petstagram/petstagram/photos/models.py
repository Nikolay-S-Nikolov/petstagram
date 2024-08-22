from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
from django.db import models

from petstagram.pets.models import Pet

SIZE_5_MB = 5 * 1024 * 1024


class ImageSizeValidator(BaseValidator):

    def __init__(self, limit_value):
        super().__init__(limit_value,
                         f"The maximum file size that can be uploaded is {limit_value / 1024 / 1024:.0f} MB.")

    def compare(self, file_size, max_size):
        return file_size > max_size

    def clean(self, x):
        return x.size


def validate_file_size_less_than_5_mb(value):
    if value.size > SIZE_5_MB:
        raise ValidationError("The maximum file size that can be uploaded is 5 MB.")


class PetPhoto(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    photo = models.ImageField(
        upload_to="pet_photos/",
        validators=[
            # validate_file_size_less_than_5_mb,
            ImageSizeValidator(SIZE_5_MB)
        ],
    )  # pip install Pillow

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=[MinLengthValidator(MIN_DESCRIPTION_LENGTH), ],
        null=True,
        blank=True
    )

    location = models.CharField(max_length=MAX_LOCATION_LENGTH)

    pets = models.ManyToManyField(Pet)

    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)
