from django import template
register = template.Library()

def is_owner(user, obj):
    if user.is_authenticated() is False or 'is_owned_by' not in dir(obj):
        return False

    if user.is_staff or obj.is_owned_by(user):
        return True
    else:
        return False

register.filter('is_owner', is_owner)
