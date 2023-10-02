from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9x345=z3oc^z_bxx0&@fp#9%-vj+im-$7kt@@ssdb2sxumeyb#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS = ['https://*.seplag.pe.gov.br', 'https://*.127.0.0.1']
ALLOWED_HOSTS = ["*"]
CSRF_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appPainel',
    "import_export",
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

ROOT_URLCONF = 'sitePainel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'sitePainel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


if os.environ.get('ENV') == "PROD":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'painel_prod',
            'USER': 'ncd_seplag',
            'PASSWORD': 'seplagncd',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

elif os.environ.get('ENV') == "DEV":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'painel_de_controle',
            'USER': 'postgres',
            'PASSWORD': 'post1234',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = 'static/'
#STATIC_ROOT = BASE_DIR / 'static'
#STATIC_ROOT = ''
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

#STATICFILES_DIRS = ('static',)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/admin'),  # Include shared static files
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "SEGES",
    "site_header": "SEGES", 
    "site_brand": "SEGES",
    "site_logo": "vendor/adminlte/img/seplagtransparente.png",
    "login_logo": "vendor/adminlte/img/seplagtransparente_login.png",
    "site_logo_classes": "squared",
    "site_icon": "vendor/adminlte/img/favicon.png",
    "welcome_sign": "Bem-vindo(a)",
    "copyright": "Instituto de Gestão Pública de Pernambuco",
    "order_with_respect_to": [
        "auth", 
        "appPainel",
        "appPainel.Eixo",
        "appPainel.Programa",
        "appPainel.Acao",
        "appPainel.Fonte",
        "appPainel.Iniciativa",
        "appPainel.Etapa",
        "appPainel.Monitoramento",
        "appPainel.MonitoramentoEtapa",
        "appPainel.Secretaria",
        "appPainel.Orgao",
        "appPainel.Responsavel",
        ],
    "show_ui_builder": False,
    "changeform_format": "vertical_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}