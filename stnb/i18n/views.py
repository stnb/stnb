# -*- coding: utf-8 -*-
import re
from urllib.parse import urlparse

from django import http
from django.conf import settings
from django.urls import resolve, reverse
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
    next_url = request.POST.get('next', request.GET.get('next', None))
    if not next_url:
        next_url = request.META.get('HTTP_REFERER', None)
    if not next_url:
        next_url = '/'

    old_lang = get_language()
    lang_code = request.GET.get('language', None)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        path = urlparse(next_url).path
        if path[0:len(old_lang)+2] == '/%s/' % old_lang:
            next_url = re.sub(path, '/%s/' % lang_code + path[len(old_lang)+2:], next_url)
            path = '/%s/' % lang_code + path[len(old_lang)+2:]
    response = http.HttpResponseRedirect(next_url)

    if lang_code and check_for_language(lang_code):
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            lang_code,
            max_age=settings.LANGUAGE_COOKIE_AGE if hasattr(settings, 'LANGUAGE_COOKIE_AGE') else None,
            path=settings.LANGUAGE_COOKIE_PATH if hasattr(settings, 'LANGUAGE_COOKIE_PATH') else '/',
            domain=settings.LANGUAGE_COOKIE_DOMAIN if hasattr(settings, 'LANGUAGE_COOKIE_DOMAIN') else None,
        )

    return response
