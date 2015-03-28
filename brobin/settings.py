"""
Django settings for brobin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from brobin.local_settings import *
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = LOCAL_SECRET_KEY

DEBUG = LOCAL_DEBUG

TEMPLATE_DEBUG = LOCAL_TEMPLATE_DEBUG

ALLOWED_HOSTS = LOCAL_ALLOWED_HOSTS

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'brobin.urls'

WSGI_APPLICATION = 'brobin.wsgi.application'

DATABASES = LOCAL_DATABASES

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = LOCAL_STATIC_ROOT
STATIC_URL = LOCAL_STATIC_URL

STATICFILES_DIRS = (
    BASE_DIR + '/brobin/static/',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/blog/templates/',
)
