# Import default settings
from mentor.settings import *

gettext = lambda s: s
_ = lambda s: s

# INSTALLED APPS EXTENSION
#
INSTALLED_APPS = INSTALLED_APPS + (

)

# EASY THUMBNAILS
#

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = True

# CMS SETTINGS
#

CMS_TEMPLATES = (
    # ('right-sidebar.html', 'With sidebar'),
    # ('fullwidth.html', 'Full width'),
    ('home.html', 'Home page'),
    ('page.html', 'Default page'),
    ('contacts.html', 'Contacts page'),
)

# Avoid new page to inheritate the template from parent (home) and force them to be right-sided by default
CMS_TEMPLATE_INHERITANCE = False

TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

# BLOG SETTINGS
#
# Make sure we do NOT use placeholders for the blog
BLOG_USE_PLACEHOLDER = True
BLOG_POSTS_LIST_TRUNCWORDS_COUNT = 20
