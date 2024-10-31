from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetCreateView(views.CreateView):
    # model = Pet # - it is not needed as form_class is used
    form_class = PetCreateForm
    template_name = "pets/create_pet.html"

    def get_success_url(self):
        return reverse(
            'details pet',
            kwargs={
                "username": "Nikolay",
                "slug": self.object.slug
            })

    # def form_valid(self, form):
    #     pet = form.save(commit=False)
    #     pet.user = self.request.user
    #     pet.save()
    #     return super().form_valid(form)

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.instance.user = self.request.user
    #     return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetDetailView(views.DetailView):
    model = Pet
    queryset = Pet.objects.all().prefetch_related(
        "petphoto_set"
    ).prefetch_related("petphoto_set__photolike_set"
                       ).prefetch_related("petphoto_set__pets")
    template_name = "pets/details_pet.html"
    slug_url_kwarg = "slug"


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/edit_pet.html"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse(
            "details pet",
            kwargs={
                "username": self.kwargs["username"],
                "slug": self.kwargs["slug"]
            }
        )


class PetDeleteView(views.DeleteView):
    model = Pet
    template_name = "pets/delete_pet.html"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs["slug"])

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["instance"] = self.object
    #     return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetDeleteForm(instance=self.object)
        return context
