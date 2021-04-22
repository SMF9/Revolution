import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# I recommend you to keep DEBUG on False. Unless you want to test things...
DEBUG = False
PROD = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Keep that Secret! Shhh. Generate one in https://djecrety.ir/
SECRET_KEY = ''

# Allowed hosts. Necessary.
ALLOWED_HOSTS = [ 'localhost', 'example.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	# pip3 install django-markdown-deux django-markdown2
    # Yes I'm using Markdown. At least I'm trying to.
	'markdown_deux',
    'revolution_main',
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

ROOT_URLCONF = 'revolution.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'revolution.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Logins, Signups and Users.

AUTH_USER_MODEL = 'revolution_main.User'
CSRF_FAILURE_VIEW = 'revolution_main.views.csrf_fail'
FORCE_LOGINS = False                # If you want to make every page redirect to /login/, change to True.
ALLOW_SIGNUPS = True                # If you want to disable signups, change to False.

# Login URL & Redirect.
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/' 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

STATIC_URL = '/s/'

# Cloudinary. Use this or Local Images feature.
cloudinary_key = None
cloudinary_secret = None
cloudinary_name = None

# Media Root
# This MUST end with a trailing slash and there must be an 'rm' folder in it
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/i/'

# reCAPTCHA v2 keys. Keep on None for no bot verification.
recaptcha_pub = None
recaptcha_priv = None

# Memo title and message on communities list
memo_title1 = "Revolution"
memo_msg1 = "Welcome to Revolution! Revolution is a Miiverse Clone programmed in Python, using a bit of Closedverse's Code (Mostly the CSS, even if that is ALSO going to be changed later too)."
memo_title2 = "MEMO_TITLE_2"
memo_msg2 = "MEMO_MSG_2"

# IPHub Key. If you do not know what is IPHub do not use it.
iphub_key = None

# If IP can be checked, then use this to disallow any proxies
disallow_proxy = False

# MD
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": "escape",
    },
}

# Force logins everywhere.
force_login = True
# Don't change this.
LOGIN_EXEMPT_URLS = (
	r'^login/$',
	r'^signup/$',
	r'^logout/$',
	r'^reset/$',
	r'^help/rules$',
	r'^help/contact$',
	r'^help/login$',
)
# The location to redirect to if a user's status is set to 2 (Redirect)
inactive_redirect = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Option to delete image if it's local
# 0 - keep, 1 - move to 'rm' folder, 2 - DELETE
image_delete_opt = 2

