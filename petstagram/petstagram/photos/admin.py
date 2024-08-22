from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "location", "created_at", "short_description", "tagged_pets")

    @staticmethod
    def short_description(obj):
        return obj.description[:20]

    @staticmethod
    def tagged_pets(obj):
        return ", ".join(pet.name for pet in obj.pets.all())
