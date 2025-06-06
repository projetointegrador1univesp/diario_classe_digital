"""
Django settings for diario_classe project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1#m%_!aph(^#4s%@3@vf38vyfqn6(-j+n6#@)x$2ogdz=1)3qs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'site_admin',
    'core',
    "admin_interface",
    "colorfield",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# Configurações específicas do admin_interface
ADMIN_INTERFACE_CONFIG = {
    'theme': 'light',  # Pode ser 'default', 'dark', 'light', etc.
    'name': 'DIÁRIO DE CLASSE DIGITAL',  # Nome personalizado
    'logo': 'static/images/logo-escola.png',  # Caminho para seu logo (opcional)
    'default_theme': {
            'css_header_background_color': '#2A3F54',
            'css_header_text_color': '#FFFFFF',
            # ... todas as outras configurações do tema ...
        }
}


# Configuração do admin_interface para sobrescrever admin padrão
ADMIN_SITE_HEADER = "DIÁRIO DE CLASSE DIGITAL"
ADMIN_SITE_TITLE = "Painel Administrativo"
ADMIN_INDEX_TITLE = "Bem-vindo ao Painel de Controle"

MIDDLEWARE = [

    'core.middleware.ModalLoginMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'diario_classe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'diario_classe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'classe_digital_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',  # ou o endereço do seu servidor MySQL
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'pt-br'  # Define o idioma como português brasileiro
TIME_ZONE = 'America/Sao_Paulo'  # Ajuste para o fuso horário do Brasil
USE_I18N = True  # Ativa a internacionalização
USE_L10N = True  # Ativa a localização
USE_TZ = True  # Ativa o suporte a fuso horário

# Arquivos estáticos e de mídia
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
