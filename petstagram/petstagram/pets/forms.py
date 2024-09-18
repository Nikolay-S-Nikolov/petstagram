from django import forms
from django.core.exceptions import ValidationError

from petstagram.core.form_mixins import ReadOnlyFieldsMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'pet_photo']
        labels = {
            "name": 'Pet name',
            "pet_photo": "Link to image",
        }
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Pet name'}),
            "date_of_birth": forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy'}),
            "pet_photo": forms.URLInput(attrs={'placeholder': 'LInk to image'}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(ReadOnlyFieldsMixin, PetBaseForm):
    read_only_fields = ("date_of_birth",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_read_only_fields()

    def clean_date_of_birth(self):
        # date_of_birth = self.cleaned_data["date_of_birth"]
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError("Date of birth is read only")
        return self.instance.date_of_birth


class PetDeleteForm(ReadOnlyFieldsMixin, PetBaseForm):
    read_only_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_read_only_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

