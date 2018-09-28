# -*- coding: utf-8 -*-
import os
import dj_database_url
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'SET THIS!')

if os.environ.get('ADMIN_NAME'):
    ADMINS = ((os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),)
    MANAGERS = ADMINS

if os.environ.get('SERVER_EMAIL'):
    SERVER_EMAIL = os.environ['SERVER_EMAIL']

if os.environ.get('EMAIL_HOST'):
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = False

ALLOWED_HOSTS = ['animatronio.com', 'www.animatronio.com']

ROOT_URLCONF = 'animatronio.urls'

WSGI_APPLICATION = 'animatronio.wsgi.application'

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Bratislava'

USE_I18N = False

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'j.n.Y'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',

    'core',
    'taggit',
    'honeypot',
]


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

HONEYPOT_FIELD_NAME = 'name'

LOGGING = {}

import django_heroku
django_heroku.settings(locals(), staticfiles=False)

LOGGING['loggers'][''] = {
    'handlers': ['console'],
    'level': 'INFO'
}
LOGGING['loggers']['django'] = {
    'handlers': ['console'],
    'level': 'INFO'
}

STATIC_ROOT = '/app/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/app/media/'
MEDIA_URL = '/media/'

DATABASES['default'] = dj_database_url.config(
    conn_max_age=django_heroku.MAX_CONN_AGE, ssl_require=False)
