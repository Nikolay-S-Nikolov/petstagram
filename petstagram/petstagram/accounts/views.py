from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import CreateUserForm, PetstagramUserLoginForm, ProfileEditForm
from petstagram.accounts.models import Profile

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


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = "accounts/edit_profile.html"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("details_profile", kwargs={"pk": self.object.pk})


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = "accounts/details_profile.html"

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_likes"] = sum([photo.photolike_set.count() for photo in self.object.user.petphoto_set.all()])
        return context


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user