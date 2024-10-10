from django import forms

from petstagram.core.form_mixins import ReadOnlyFieldsMixin
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ["photo", "description", "location", "pets"]
        labels = {
            "photo": 'Photo file',
            "pets": "Tag Pets",
        }
        widgets = {
            "description": forms.TextInput(attrs={'placeholder': 'Photo description here...'}),
            "location": forms.TextInput(attrs={'placeholder': 'Photo shooting location here..'}),
        }


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(PetPhotoBaseForm, ReadOnlyFieldsMixin):
    read_only_fields = ("photo",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_read_only_fields()


class PetPhotoDeleteForm(PetPhotoBaseForm, ReadOnlyFieldsMixin):
    read_only_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_read_only_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
