"""
Django settings for SuperPizzas project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from SuperPizzas.utils import load_env_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "$(@^69=kndq*xgwx=)oehr0atm(n99e6o1mobk=wvx^=j84#d+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".localhost"]

AUTH_USER_MODEL = "users.User"
# Application definition

SHARED_APPS = (
    "django_tenants",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_jenkins",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "captcha",
    "bootstrap3",
    "django_select2",
    "simple_history",
    "public_view",
    "franchises",
    "users",
    "social_django",
)


TENANT_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_jenkins",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "captcha",
    "bootstrap3",
    "django_select2",
    "simple_history",
    "pizzas",
    "users",
    "social_django",
)

INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))


JENKINS_TASKS = ("django_jenkins.tasks.run_pep8", "django_jenkins.tasks.run_pyflakes")
PROJECT_APPS = []

TENANT_MODEL = "franchises.Franchise"  # app.Model

TENANT_DOMAIN_MODEL = "franchises.Domain"  # app.Model

MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "public_view.middleware.FranchiseValidityMiddleware",
]

ROOT_URLCONF = "SuperPizzas.tenant_urls"
PUBLIC_SCHEMA_URLCONF = "SuperPizzas.public_urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "SuperPizzas.wsgi.application"

# ---
# Social Auth Feature
AUTHENTICATION_BACKENDS = [
        'social_core.backends.linkedin.LinkedinOAuth2',
        'social_core.backends.instagram.InstagramOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    ]

SOCIAL_AUTH_FACEBOOK_KEY = "975746819426741"
SOCIAL_AUTH_FACEBOOK_SECRET = "18f4cba9bb2cbe58fb7908ac014ea07a"

# ---


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

POSTGRES_HOST = "127.0.0.1"
POSTGRES_PORT = 5432
POSTGRES_DB = "superpizzas"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"


# settings set via env/secrets.env
REPO_DIR = os.path.dirname(BASE_DIR)
ENV_DIR = os.path.join(BASE_DIR, "env")
ENV_SECRETS_FILE = os.path.join(ENV_DIR, "secrets.env")
ENV_SECRETS = load_env_settings(dotenv_path=ENV_SECRETS_FILE, defaults=globals())
globals().update(ENV_SECRETS)

DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "NAME": POSTGRES_DB,
    }
}

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "..", "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")
MEDIA_URL = "/media/"

MAX_FILE_SIZE = 10485760  # 10MB

DOMAIN = "localhost"


RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
NOCAPTCHA = True
# LOGIN/LOGOUT/SIGN-UP
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = "home"
