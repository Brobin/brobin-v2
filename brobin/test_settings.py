import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCAL_SECRET_KEY = 'secret_key_lololol'

LOCAL_ALLOWED_HOSTS = ['*']

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

LOCAL_DEBUG = True

LOCAL_TEMPLATE_DEBUG = True

LOCAL_STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'brobin/static'),
]

LOCAL_STATIC_URL = '/static/'

LOCAL_STATIC_ROOT = os.path.join(BASE_DIR, 'static')
