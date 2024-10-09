from django import forms

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


class PetPhotoEditForm(PetPhotoBaseForm):
    pass
