import re
from urlparse import urlparse

from django import http
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import check_for_language, activate, to_locale, get_language


def set_language(request):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
        
    old_lang = get_language()
    lang_code = request.GET.get('language', None)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        path = urlparse(next).path
        if path[0:len(old_lang)+2] == '/%s/' % old_lang:
            next = re.sub(path, '/%s/' % lang_code + path[len(old_lang)+2:], next)
            path = '/%s/' % lang_code + path[len(old_lang)+2:]
    response = http.HttpResponseRedirect(next)

    return response

