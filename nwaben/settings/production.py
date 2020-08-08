"""
Django settings for nwaben project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import cloudinary
from nwaben.cloudinary_settings import *

AUTH_USER_MODEL = "accounts.User"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k@g(@6x!5+6-4dfw9*p(1c@bc^6g22t9w&uh6c4hw-9jj-x($('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    # custom apps
    'accounts.apps.AccountsConfig',
    'articles.apps.ArticlesConfig',
    'archive.apps.ArchiveConfig',

    # third party apps
    'widget_tweaks',
    'rest_framework',
    'phonenumber_field',
    'crispy_forms',
    'corsheaders',
    'cloudinary_storage',
    'cloudinary',
    'ckeditor',
    'ckeditor_uploader',
    # 'audiofield',
]


CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 150,
        'width': 600,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Link', 'Unlink', 'Image', 'CodeSnippet', 'RemoveFormat', 'Source', 'Youtube'],
        ],
        'extraPlugins': ','.join(['codesnippet', 'youtube']),
    },

    'special': {
        'toolbar': 'Special',
        'height': 200,
        'toolbar_Special': [
            ['Bold', 'Italic', 'Link', 'Unlink', 'Image', 'CodeSnippet', 'Source', 'Youtube'],
        ],
        'extraPlugins': ','.join(['codesnippet', 'youtube']),
    },

    'comment_content': {
        'toolbar': 'Special',
        'height': 150,
        'width': 600,
        'toolbar_Special': [
            ['Bold', 'Italic', 'Link', 'Unlink'],
        ],
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'audiofield.middleware.threadlocals.ThreadLocals',
]

ROOT_URLCONF = 'nwaben.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'nwaben.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd36gr1q5ja7r0m',
        'USER': 'jqemoxdxonkqau',
        'PASSWORD': '2ea8750dadeac43f15aefa0f9ce59e988e67d606d774458360e5a13ed710b8ea',
        'HOST': 'ec2-34-206-252-187.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_ROOT = MEDIA_URL

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_CLASS_CONVERTERS = {
    'textinput': "form-control",
    'urlinput': "form-control",
    'numberinput': "form-control",
    'emailinput': "form-control",
    'dateinput': "form-control",
    'textarea': "form-control",
    'passwordinput': "form-control",
    'select': "form-control",
}

# Heroku cloud upload settings...
django_heroku.settings(locals())

# Https settings...
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = None
SESSION_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True

# config/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = "username_email"
