from django import template

register = template.Library()


@register.filter
def is_liked_by_user(photo, user):
    if photo.photolike_set.filter(user=user).exists():
        return True
    return False
