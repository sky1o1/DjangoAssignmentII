from .base import *

SECRET_KEY = 'c_%lx8e%uq99x_n1!0od2fv3znq$$k*w-x_w!klt^j=%!evekn'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '907e30a513ddef'
EMAIL_HOST_PASSWORD = 'ee3e4e0174d4af'
EMAIL_PORT = '2525'

# AUTH_USER_MODEL = 'blogger.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


