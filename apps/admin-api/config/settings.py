"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from typing import Any, List

import environ
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# envファイル設定(testcase実行時そうでない時で読み込むenvファイルを変える)
env = environ.Env()
env_name = ".env"
if os.getenv("TESTING") == "1":
    env_name = ".env.testing"
env.read_env(os.path.join(BASE_DIR, env_name))

APP_ENV = env.str("APP_ENV", default="production")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="hoge")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS: List[str] = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
    "corsheaders",
    # 作成したアプリを追加していく
    "app.hc.apps.HcConfig",
    "app.core.apps.CoreConfig",
    "app.accounts.apps.AccountConfig",
    "app.admin_users.apps.AdminUserConfig",
    "app.users.apps.UserConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.str("DATABASE_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "ja"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.WatchedFileHandler",
            "filename": BASE_DIR / "logs/django.log",
        },
        "sql_file": {
            "level": "DEBUG",
            "class": "logging.handlers.WatchedFileHandler",
            "filename": BASE_DIR / "logs/query.log",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
        "django.db.backends": {
            "handlers": ["sql_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# 下記の設定のどちらかが必要
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]

# django_rest
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "app.core.authentications.custom_jwt_authentications.CustomJWTAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "EXCEPTION_HANDLER": "app.core.exceptions.custom_exception_handler",
}

# AUTH_USER_MODEL = "admin_users.AdminUser"

AWS: Any = {
    "DEFAULT": {},
    "S3": {
        "DEFAULT": {
            "AWS_ACCESS_KEY_ID": env.str("AWS_ACCESS_KEY_ID", default=""),
            "AWS_SECRET_ACCESS_KEY": env.str("AWS_SECRET_ACCESS_KEY", default=""),
            "AWS_REGION": env.str("AWS_DEFAULT_REGION", default="ap-northeast-1"),
            "AWS_BUCKET": env.str("AWS_BUCKET", default="production"),
            "AWS_S3_EXPIRATION_TIME": env.int("AWS_S3_EXPIRATION_TIME", default=300),
        }
    },
}


# デバッグ
if DEBUG and os.environ.get("RUN_MAIN") or os.environ.get("WERKZEUG_RUN_MAIN"):  # noqa
    import debugpy

    debugpy.listen(("0.0.0.0", 9000))

AUTH_USER_MODEL = "admin_users.AdminUser"

# 認証
AUTH_APP_NAME = "admin_users"
AUTH_MODEL_NAME = "AdminUser"
JWT_ACCESS_TOKEN_EXPIRES_SECONDS = 3600 * 24 * 7
JWT_REFRESH_TOKEN_EXPIRES_SECONDS = 3600 * 24 * 14
JWT_ALGORITHM = "HS256"

# メールバックエンド設定
EMAIL_BACKEND = env.str("EMAIL_BACKEND", default="")
EMAIL_HOST = env.str("EMAIL_HOST", default="")
EMAIL_PORT = env.str("EMAIL_PORT", default="")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)

FRONTEND_API_URL = env.str("FRONTEND_API_URL", default="")