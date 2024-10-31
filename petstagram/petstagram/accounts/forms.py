from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from petstagram.accounts.models import Profile

UserModel = get_user_model()


class CreateUserForm(auth_forms.BaseUserCreationForm):
    # if not created custom filter to add placeholder to form fields
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["email"].widget.attrs['placeholder'] = 'Email'
    #     self.fields["password1"].widget.attrs['placeholder'] = 'Password'
    #     self.fields["password2"].widget.attrs['placeholder'] = 'Repeat Password'

    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2']


class PetstagramUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'


class PetstagramUserLoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus": True}))


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth (YYYY-MM-DD)',
            'profile_picture': 'Profile Picture',
        }
