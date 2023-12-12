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
#    'smart_selects',
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
STATIC_ROOT = ''
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

#STATICFILES_DIRS = ('static',)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/admin'),
      'static',  # Include shared static files
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "filters_position": "right",
    "site_title": "SEGES",
    "site_header": "SEGES", 
    "site_brand": " ",
    "site_logo": "vendor/adminlte/img/seplagtransparente.png",
    "site_logo_classes": "squared",
    "login_logo": "vendor/adminlte/img/seplagtransparente_login.png",
    "site_icon": "vendor/adminlte/img/favicon.png",
    "welcome_sign": "Bem-vindo(a)",
    "copyright": "Instituto de Gestão Pública de Pernambuco",
    "topmenu_links": [
        {"name": "Início",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Suporte", "url": "https://www.seplag.pe.gov.br/contato", "new_window": True},
        {"model": "auth.User"},
        {"app": "appPainel"},
    ],
    "order_with_respect_to": [
        "auth", 
        "appPainel",
        "appPainel.Eixo",
        "appPainel.Programa",
        "appPainel.Acao",
        "appPainel.Fontes",
        "appPainel.Secretaria",
        "appPainel.Orgao",
        "appPainel.Responsavel",
        "appPainel.Municipio",
        "appPainel.Produto",
        "appPainel.Ano",
        "appPainel.TipoPrograma",
        "appPainel.TipoAcao",
        "appPainel.Tipo",
        "appPainel.Tema",
        "appPainel.Status",   
        "appPainel.Meta",
        "appPainel.Etapa",
        "appPainel.Subetapa",
        "appPainel.Monitoramento",
        "appPainel.MonitoramentoEtapa",
        "appPainel.MonitoramentoSubetapa",
        ],
    "show_ui_builder": False,
    
    ##BUSCA
    "search_bar": True,
    "search_model": ["appPainel.Meta"],
    
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible",
    },
    #### BARRA LATERAL ####
    
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "appPainel.Monitoramento": "fas fa-calendar",
        "appPainel.MonitoramentoEtapa": "fas fa-calendar",
        "appPainel.MonitoramentoSubEtapa": "fas fa-calendar",
        "appPainel.Eixo": "fas fa-wallet",
        "appPainel.Programa": "fas fa-wallet",
        "appPainel.Acao": "fas fa-wallet",
        "appPainel.Fontes": "fas fa-wallet",
        "appPainel.Secretaria": "fas fa-building",
        "appPainel.Orgao": "fas fa-building",
        "appPainel.Responsavel": "fas fa-user-tie",
        "appPainel.Municipio": "fas fa-city",
        "appPainel.Produto": "fas fa-warehouse",
        "appPainel.Ano": "fas fa-clock",
        "appPainel.Tema": "fas fa-list",
        "appPainel.Status": "fas fa-list",
        "appPainel.TipoPrograma": "fas fa-list",
        "appPainel.TipoAcao": "fas fa-list",
        "appPainel.Tipo": "fas fa-list",
        "appPainel.Meta": "fas fa-chart-bar",
        "appPainel.Etapa": "fas fa-chart-bar",
    },
    
    "default_icon_children": "fas fa-square",

    "show_sidebar": True,
    "navigation_expanded": False,
    "search_models": [
        {"app": "appPainel", "model": "Meta"},
    ],
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
    "navbar_fixed": True,
    "layout_boxed": True,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": 'sidebar-light-navy',
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    #"theme": "sandstone",
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-primary"
    },
    "actions_sticky_top": False
}

QUERY_URL = True