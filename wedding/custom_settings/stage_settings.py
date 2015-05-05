AWS = True
from mentor.custom_settings.applications_settings import *

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jonas_test',
        'USER': 'britny',
        'PASSWORD': 'I6bjUnpH83gW',
        'HOST': 'britnystage.c3wi05pwmygc.eu-west-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}
STATICFILES_DIRS = ()
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

