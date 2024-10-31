from django.contrib.auth import get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import CreateUserForm, PetstagramUserLoginForm, ProfileEditForm

UserModel = get_user_model()


class SignupUser(views.CreateView):
    model = UserModel
    form_class = CreateUserForm
    template_name = "accounts/signup_user.html"
    success_url = reverse_lazy("index")


class PetstagramLoginView(auth_views.LoginView):
    form_class = PetstagramUserLoginForm
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True


class PetstagramLogoutView(auth_views.LogoutView):
    pass


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = "accounts/edit_profile.html"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("details_profile", kwargs={"pk": self.object.pk})


def details_profile(request, pk):
    context = {}
    return render(request, "accounts/details_profile.html", context)


def delete_profile(request, pk):
    context = {}
    return render(request, "accounts/delete_profile.html", context)
