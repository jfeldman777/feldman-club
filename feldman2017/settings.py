"""
Django settings for feldman2017 project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from django.utils.translation import ugettext_lazy as _
import os
from machina import get_apps as get_machina_apps
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR

# Tell Django where the project's translation files should be.
SITE_ID = 1

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
}
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qi_114_xi5%3f^e@-qrg5amv116oaxrq4(@-(&xq0m2^872cx7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['feldman-club.herokuapp.com',
        'localhost',
        '127.0.0.1',
    ]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Application definition
#LOGIN_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = '/'

SMARTFIELDS_KEEP_ORPHANS = False

INSTALLED_APPS = [
    'club.apps.ClubConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'tagging',
    'zinnia',
     # Machina related apps:
    'mptt',
    'haystack',
    'widget_tweaks',

    'quiz',
    'multichoice',
    'true_false',
    'essay',
    'int_question',
] + get_machina_apps()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
     # Machina
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
]

ROOT_URLCONF = 'feldman2017.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',
                MACHINA_MAIN_TEMPLATE_DIR,
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'zinnia.context_processors.version',  # Optional
                 # Machina
                'machina.core.context_processors.metadata',
            ],

            #'loaders': [######################
            #    'django.template.loaders.filesystem.Loader',
            #    'django.template.loaders.app_directories.Loader',
            #]################
        },
    },
]

WSGI_APPLICATION = 'feldman2017.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

UP = True
try:
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST= 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
except:
    UP = False
    pass

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGOUT_REDIRECT_URL = '/'

#reset password tools
'''
Also needed is the Python command line email server:
python -m smtpd -n -c DebuggingServer localhost:2525
'''
if DEBUG:
    EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = 'localhost', 2525, None, None
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
#STATIC_HOST = 'https://d2mjsx616o8pj3.cloudfront.net' if UP else ''
STATIC_URL = '/static/'

STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
            MACHINA_MAIN_STATIC_DIR,
        ]


STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, "staticfiles"))
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
try:
    AWS_S3_HOST = "s3-us-west-1.amazonaws.com"
    AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', '')
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_REGION = os.environ.get('AWS_REGION', '')
    AWS_S3_CALLING_FORMAT = "boto.s3.connection.OrdinaryCallingFormat"
    AWS_PRELOAD_METADATA = True
    MEDIA_URL = 'https://s3-%s.amazonaws.com/%s/media/' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
    #DEFAULT_FILE_STORAGE = 'myapp.customstorages.MediaStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    MEDIAFILES_LOCATION = 'media'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = 'https://' + AWS_S3_CUSTOM_DOMAIN+'/'
except:
    pass
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
