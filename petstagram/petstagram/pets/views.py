from django.shortcuts import render


def create_pet(request):
    context = {

    }
    return render(request, "pets/create_pet.html")


def details_pet(request, username, pet_slug):
    context = {

    }
    return render(request, "pets/details_pet.html")


def edit_pet(request, username, pet_slug):
    context = {

    }
    return render(request, "pets/edit_pet.html")


def delete_pet(request, username, pet_slug):
    context = {

    }
    return render(request, "pets/delete_pet.html")
