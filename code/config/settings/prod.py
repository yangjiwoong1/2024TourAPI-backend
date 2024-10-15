from .base import *

BACKEND_URL = env('BACKEND_URL')
DATABASE_ENGINE = env('DATABASE_ENGINE')
DATABASE_SCHEMA = env('DATABASE_SCHEMA')
DATABASE_USER = env('DATABASE_USER')
DATABASE_USER_PASSWORD = env("DATABASE_USER_PASSWORD")
DATABASE_HOST = env('DATABASE_HOST')
DATABASE_PORT = env('DATABASE_PORT')
# For CORS
FRONTEND_URL = env('FRONTEND_URL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [BACKEND_URL]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', # authenticated
    )
}

# prod_setting
DATABASES = {
    'default' : {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_SCHEMA,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_USER_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

# CORS 설정
CORS_ALLOWED_ORIGINS = [
    FRONTEND_URL,
]