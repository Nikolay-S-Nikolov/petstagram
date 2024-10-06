from django.urls import path, include

from petstagram.pets.views import details_pet, edit_pet, delete_pet, PetCreateView

urlpatterns = (
    path('create/', PetCreateView.as_view(), name='create pet'),
    path('<str:username>/pet/<slug:slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ])),
)

