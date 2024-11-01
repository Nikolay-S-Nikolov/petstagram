from django import forms

from petstagram.common.models import PhotoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment

        fields = ("text",)

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'name': 'body',
                    'class': 'form-control',
                    'cols': '40',
                    'rows': '10',
                    'placeholder': 'Add comment...',
                    'maxlength': '300',
                    'id': 'id_body',
                }
            )
        }
