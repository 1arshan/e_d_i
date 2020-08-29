"""
Django settings for adcbackend project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from .secrets import ProjectSecretKey, DatabaseSecretLocal, Cloud ,DatabaseSecretCloud
import os
import urllib.parse
import djcelery
from kombu.utils.url import safequote

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#aws_access_key = safequote("AKIA5VSMNQIOHBY")
#aws_secret_key = safequote("x4ZbVgb6q2GvALJL+4GqEHV+oN/WdvaV")
djcelery.setup_loader()

#CELERY_TASK_DEFAULT_QUEUE = 'edifi-server5-queque'
#BROKER_URL = "sqs://{aws_access_key}:{aws_secret_key}@https://sqs.ap-south-1.amazonaws.com/939684365768/edifi-server5-queque".format(
 #   aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
#)
#CELERY_BROKER_TRANSPORT_OPTIONS = {
 #   'region': 'ap-south-1',
#}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ProjectSecretKey.project_secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = Cloud.allowed_host
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # -----third party app ------->>
    'django_better_admin_arrayfield',
    'storages',

    # -----user define app ------>
    'user_signup',
    'broadcaster',
    'subject_material',
    'user_login',
    'administration',
    'classroom',

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

ROOT_URLCONF = 'adcbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'adcbackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': DatabaseSecretLocal.engine,
        'NAME': DatabaseSecretLocal.name,
        'USER': DatabaseSecretLocal.user,
        'PASSWORD': DatabaseSecretLocal.password,
        'HOST': DatabaseSecretLocal.host,
        'PORT': DatabaseSecretLocal.port,
        }
    }

"""
DATABASES = {
    'default': {
        'ENGINE': DatabaseSecretCloud.engine,
        'NAME': DatabaseSecretCloud.name,
        'USER': DatabaseSecretCloud.user,
        'PASSWORD': DatabaseSecretCloud.password,
        'HOST': DatabaseSecretCloud.host,
        'PORT': DatabaseSecretCloud.port,
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AWS_ACCESS_KEY_ID = 'AKIA5VSMNQXEDXCBGXPD'
AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'edifi-server5-bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static-production'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'adcbackend/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'adcbackend.storage_backends.MediaStorage'
