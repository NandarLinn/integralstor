"""
Django settings for the integral_view project.

Generated by 'django-admin startproject' using Django 1.8.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from integralstor import config
platform_root, err = config.get_platform_root()

TEMPLATE_DIR_PATH_LIST = ["%s/integral_view/templates"%platform_root, "%s/integral_view/core/storage/templates"%platform_root, "%s/integral_view/core/replication/templates"%platform_root, "%s/integral_view/core/tasks/templates"%platform_root, "%s/integral_view/core/keys_certs/templates"%platform_root, "%s/integral_view/core/networking/templates"%platform_root, "%s/integral_view/core/users_groups/templates"%platform_root, "%s/integral_view/core/storage_access/templates"%platform_root, "%s/integral_view/core/system/templates"%platform_root, "%s/integral_view/core/monitoring/templates"%platform_root, "%s/integral_view/core/application_management/templates"%platform_root]

import os
ROOT_PATH = os.path.dirname(__file__)
STATIC_DIR_PATH_LIST = [os.path.join(ROOT_PATH, 'static')]

applications, err = config.get_applications_config()
application_template_dirs = []
application_static_dirs = []
if applications:
    for base_dir, app in list(applications.items()):
        application_template_dirs.append('%s/integral_view/applications/%s/templates'%(platform_root, base_dir))
        application_static_dirs.append('%s/integral_view/static/%s'%(platform_root, base_dir))

if application_template_dirs:
    TEMPLATE_DIR_PATH_LIST.extend(application_template_dirs)
if application_static_dirs:
    STATIC_DIR_PATH_LIST.extend(application_static_dirs)


LOGIN_URL = '/login/'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jycl#9_@i^fvbgnk)p&^%2-(8o#u2%*3iono7q9_i2%&z)q!7-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'integral_view',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'integral_view.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIR_PATH_LIST,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'integral_view.context_processors.get_version',
                'integral_view.context_processors.get_brand_config'
            ],
        },
    },
]

WSGI_APPLICATION = 'integral_view.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'config/db/django.db'),
    },
    'integralstor': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'config/db/integralstor.db'),
    },
    'inotify': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'config/db/inotify.db'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = STATIC_DIR_PATH_LIST

# vim: tabstop=8 softtabstop=0 expandtab ai shiftwidth=4 smarttab
