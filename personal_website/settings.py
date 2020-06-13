"""
Django settings for personal_website project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the default to production since it’s always
# good to default to production settings, otherwise you risk deploying a project that
# has security vulnerabilities.

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')

# SECRET_KEY = os.environ.get('SECRET_KEY', 'not-so-secret-key')
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = 'a6*!0w3cffb(l-nf+z3zs@co$q%$_3m@i!l8t0^m)+xa0qtegv'
# DEBUG can be True/False or 1/0
DEBUG = int(os.environ.get('DEBUG', default=0)) 
# DEBUG = True
#ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split()

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # A better approach is to add whitenoise.runserver_nostatic 
    # before django.contrib.stataticfiles
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    # Third-party
    'pagedown.apps.PagedownConfig',
    'crispy_forms',
    'debug_toolbar',

    'projects.apps.ProjectsConfig',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'contact.apps.ContactConfig',
    'about.apps.AboutConfig',
    'newsletters.apps.NewslettersConfig',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'personal_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'personal_website/templates')
        ],
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

WSGI_APPLICATION = 'personal_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_pg_db',
        'USER': 'postgres',
        'PASSWORD': 'bismillah_19@pg',
        'HOST': 'db',
        'PORT': 5432,
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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# These are the settings for sending email in Django via Gmail
from .email_info import EMAIL_BACKEND, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_USE_SSL
EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD 
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_USE_SSL = EMAIL_USE_SSL


# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

# production
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_REFERRER_POLICY='origin'


# Heroku
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
