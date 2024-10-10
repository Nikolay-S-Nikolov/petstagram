from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm, PetPhotoDeleteForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/create_photo.html"

    def get_success_url(self):
        return reverse('details photo', kwargs={
            "pk": self.object.pk})


class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all().prefetch_related(
        "photocomment_set"
    ).prefetch_related("pets"
                       ).prefetch_related("photolike_set")
    template_name = "photos/details_photo.html"


#
# def details_photo(request, pk):
#     context = {
#         "pet_photo": PetPhoto.objects.get(pk=pk)
#
#     }
#     return render(request, "photos/details_photo.html", context)


class PetPhotoEditView(views.UpdateView):
    form_class = PetPhotoEditForm
    queryset = PetPhoto.objects.all()
    template_name = "photos/edit_photo.html"

    def get_success_url(self):
        return reverse('details photo', kwargs={
            "pk": self.object.pk})


class PetPhotoDeleteView(views.DeleteView):
    # form_class = PetPhotoDeleteForm
    queryset = PetPhoto.objects.all()
    template_name = "photos/delete_photo.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetPhotoDeleteForm(instance=self.object)
        return context

