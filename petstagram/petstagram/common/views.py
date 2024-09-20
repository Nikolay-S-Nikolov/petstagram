from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def index(request):
    pet_name_pattern = request.GET.get("pet_search_pattern", "")
    pet_photos = PetPhoto.objects.all()

    if pet_name_pattern:
        pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)

    context = {
        "pet_photos": pet_photos,
        "pet_name_pattern": pet_name_pattern
    }
    return render(request, 'common/home-page.html', context)


def like_pet_photo(request, pk):
    # pet_photo_like = PetPhoto.objects.filter(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()

    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META["HTTP_REFERER"] + f"#photo-{pk}")  # in order to remain on same photo f"#photo-{pk}"
