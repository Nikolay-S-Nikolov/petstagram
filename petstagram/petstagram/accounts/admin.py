from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from petstagram.accounts.forms import PetstagramUserChangeForm, CreateUserForm
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = CreateUserForm
    form = PetstagramUserChangeForm
    list_display = ['pk', 'email', 'is_staff', 'is_superuser']
    search_fields = ['email']
    ordering = ['pk']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
