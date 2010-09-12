"""
These are the default configuration options for Django-elRTE
"""

import os
from django.conf import settings

# DEFAULT_CONFIG = getattr(settings, 'ELRTE_DEFAULT_CONFIG',
#         {'theme': "simple", 'relative_urls': False})

#USE_SPELLCHECKER = getattr(settings, 'ELRTE_SPELLCHECKER', False)
#USE_COMPRESSOR = getattr(settings, 'ELRTE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'ELRTE_FILEBROWSER', False)

ELRTE_DEBUG = getattr(settings, 'ELRTE_DEBUG', False)

JS_BASE_URL = getattr(settings, 'ELRTE_JS_BASE_URL',
        os.path.join(settings.MEDIA_URL, 'elrte/js/'))

if ELRTE_DEBUG:
    URL = getattr(settings, 'ELRTE_JS_URL', '%selrte.full.js' % JS_BASE_URL)
else:
    URL = getattr(settings, 'ELRTE_JS_URL', '%selrte.min.js' % JS_BASE_URL)

LOAD_JQUERY = getattr(settings, 'ELRTE_LOAD_JQUERY', True)
LOAD_JQUERYUI = getattr(settings, 'ELRTE_LOAD_JQUERYUI', True)

JS_URL = []

if LOAD_JQUERY:
    JS_URL.append("%sjquery-1.4.2.min.js" % JS_BASE_URL)

if LOAD_JQUERYUI:
    JS_URL.append("%sjquery-ui-1.8.4.custom.min.js" % JS_BASE_URL)

JS_URL.append(URL)

CSS_URL = []
if LOAD_JQUERYUI:
    CSS_URL.append(
        "%sui-themes/smoothness/jquery-ui-1.8.4.custom.css" % JS_BASE_URL
    )

CSS_URL.extend([
    "%s../css/elrte.full.css" % JS_BASE_URL,
    "%s../css/django-elrte.css" % JS_BASE_URL,
])

ADMIN_FIELDS = getattr(settings, 'ELRTE_ADMIN_FIELDS', {})