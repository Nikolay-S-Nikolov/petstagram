from django.contrib.auth import get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import CreateUserForm

ModelUser = get_user_model()


class SignupUser(views.CreateView):
    model = ModelUser
    form_class = CreateUserForm
    template_name = "accounts/signup_user.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return result


# def signup_user(request):
#     context = {}
#     return render(request, "accounts/signup_user.html", context)


class PetstagramLoginView(auth_views.LoginView):
    form_class = auth_views.AuthenticationForm
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True


# def signin_user(request):
#     context = {}
#     return render(request, "accounts/signin_user.html", context)


def signout_user(request):
    return redirect("index")


def details_profile(request, pk):
    context = {}
    return render(request, "accounts/details_profile.html", context)


def edit_profile(request, pk):
    context = {}
    return render(request, "accounts/edit_profile.html", context)


def delete_profile(request, pk):
    context = {}
    return render(request, "accounts/delete_profile.html", context)
