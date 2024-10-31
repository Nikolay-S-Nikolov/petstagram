from django.shortcuts import render, redirect
from django.views import generic as views

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


class IndexView(views.ListView):
    queryset = PetPhoto.objects.all().prefetch_related(
        "photolike_set"
    ).prefetch_related(
        "pets"
    ).distinct()
    template_name = 'common/home-page.html'

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_search_pattern", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern or ""
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_pattern(queryset)
        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query["pets__name__icontains"] = pet_name_pattern

        return queryset.filter(**filter_query)


def like_pet_photo(request, pk):
    # pet_photo_like = PetPhoto.objects.filter(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()

    else:
        PhotoLike.objects.create(pet_photo_id=pk, user=request.user)

    return redirect(request.META["HTTP_REFERER"] + f"#photo-{pk}")  # in order to remain on same photo f"#photo-{pk}"