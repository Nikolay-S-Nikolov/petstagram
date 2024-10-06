from django.shortcuts import render, redirect
from django.urls import reverse
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


def details_pet(request, username, slug):
    context = {
        "pet": Pet.objects.get(slug=slug),
        "username": username
    }
    return render(request, "pets/details_pet.html", context)


def edit_pet(request, username, slug):
    pet_to_edit = Pet.objects.get(slug=slug)
    pet_form = PetEditForm(request.POST or None, instance=pet_to_edit)
    if request.method == 'POST' and pet_form.is_valid():
        edited_pet = pet_form.save()
        return redirect('details pet', username="Nikolay", slug=edited_pet.slug)
    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet_to_edit,
    }
    return render(request, "pets/edit_pet.html", context)


def delete_pet(request, username, slug):
    pet_to_delete = Pet.objects.get(slug=slug)
    pet_form = PetDeleteForm(request.POST or None, instance=pet_to_delete)
    if request.method == 'POST' and pet_form.is_valid():
        pet_form.save()
        return redirect('index')
    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet_to_delete,
    }
    return render(request, "pets/delete_pet.html", context)
