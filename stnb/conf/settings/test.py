# -*- coding: utf-8 -*-
"""
Test settings for running the test suite with SQLite.
"""
from .default import *

# Use SQLite for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable cachalot during tests
CACHALOT_ENABLED = False

# Remove cachalot from installed apps for testing
INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'cachalot']

# Speed up password hashing for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable debug for tests
DEBUG = False
