from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


def create_pet(request):
    pet_form = PetCreateForm(request.POST or None)
    if request.method == 'POST' and pet_form.is_valid():
        created_pet = pet_form.save()
        return redirect('details pet', username="Nikolay", pet_slug=created_pet.slug)
    context = {
        "pet_form": pet_form
    }
    return render(request, "pets/create_pet.html", context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug)
    }
    return render(request, "pets/details_pet.html", context)


def edit_pet(request, username, pet_slug):
    pet_to_edit = Pet.objects.get(slug=pet_slug)
    pet_form = PetEditForm(request.POST or None, instance=pet_to_edit)
    if request.method == 'POST' and pet_form.is_valid():
        edited_pet = pet_form.save()
        return redirect('details pet', username="Nikolay", pet_slug=edited_pet.slug)
    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet_to_edit,
    }
    return render(request, "pets/edit_pet.html", context)


def delete_pet(request, username, pet_slug):

    pet_to_delete = Pet.objects.get(slug=pet_slug)
    pet_form = PetDeleteForm(request.POST or None, instance=pet_to_delete)
    if request.method == 'POST' and pet_form.is_valid():
        pet_form.save()
        return redirect('index')
    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet_to_delete,
    }
    return render(request, "pets/delete_pet.html",context)
