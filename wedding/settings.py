"""
Django settings for mentor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
_ = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '98dluutqm)!@^4d2eh6(otm#p%e54zqac!iy1pq5!uf%#z_46^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'RsvpForm',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 'djangocms_flash',
    # 'djangocms_file',
    # 'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_link',
    'djangocms_text_ckeditor',
    # 'djangocms_column',
    # 'djangocms_grid',
    # 'djangocms_snippet',

    'cms',
    'mptt',
    'menus',
    'sekizai',
    'filer',
    'easy_thumbnails',

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'treebeard',
    'reversion',
    'parler',
    'crispy_forms',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

LANGUAGES = [
    ('sv', _('Svenska')),
]

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': True,
        'redirect_on_fallback': False,
    },
    1: [
        {
            'public': True,
            'code': 'sv',
            'hide_untranslated': True,
            'name': _('Svenska'),
            'redirect_on_fallback': True,
        },
   ],
}

PARLER_LANGUAGES = {
    1: (
        {'code': 'sv', },
    ),
    'default': {
        'hide_untranslated': True,
    }
}

MIGRATION_MODULES = {
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',

    'filer': 'filer.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
}

SITE_ID = 1
CMS_PERMISSIONS = True
ROOT_URLCONF = 'wedding.urls'

WSGI_APPLICATION = 'wedding.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'sv'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

CMS_TEMPLATES = (
    ('page.html', 'Default page'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'
TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

try:
    from wedding.custom_settings.local_settings import *
except ImportError:
    pass
