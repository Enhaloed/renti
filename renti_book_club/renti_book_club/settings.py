import os
import re

"""
Django settings for renti_book_club project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_@$+se3fwj6zg6-1w^i-0tb46^qy0mur-^%%@%gnfn0cf=lciy'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('PRODUCTION'):
    print('Running in PRODUCTION mode...')
    DEBUG = False
else:
    print('Running in DEBUG mode...')
    DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'book_club',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'renti_book_club.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'renti_book_club.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.environ.get('DATABASE_URL'):  # Heroku parsing
    db_url_re = re.compile(r'postgres:\/\/(\S+):(\S+)@(\S+):(\d+)\/(\S+)')
    re_result:list = re.findall(db_url_re, os.environ.get('DATABASE_URL'))
    match:tuple = re_result[0]

    db_user = match[0]
    db_pass = match[1]
    db_host = match[2]
    db_port = match[3]
    db_name = match[4]
else:
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': db_user,
        'NAME': db_name,
        'PASSWORD': db_pass,
        'HOST': db_host,
        'PORT': db_port
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'book_club/static/')