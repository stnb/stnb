from django import template
register = template.Library()

def is_owner(user, xerrada):
    if user.is_authenticated() is False:
        return False

    if xerrada.is_owner(user) or user.is_staff:
        return True
    else:
        return False

register.filter('is_owner', is_owner)
