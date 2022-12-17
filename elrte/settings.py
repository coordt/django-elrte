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
        os.path.join(settings.STATIC_URL, 'elrte/js/'))

CSS_BASE_URL = getattr(settings, 'ELRTE_JS_BASE_URL',
        os.path.join(settings.STATIC_URL, 'elrte/css/'))

if ELRTE_DEBUG:
    URL = getattr(settings, 'ELRTE_JS_URL', f'{JS_BASE_URL}elrte.full.js')
else:
    URL = getattr(settings, 'ELRTE_JS_URL', f'{JS_BASE_URL}elrte.min.js')

LOAD_JQUERY = getattr(settings, 'ELRTE_LOAD_JQUERY', True)
LOAD_JQUERYUI = getattr(settings, 'ELRTE_LOAD_JQUERYUI', True)

JS_URL = []

if LOAD_JQUERY:
    JS_URL.append(f"{JS_BASE_URL}jquery-1.6.1.min.js")

if LOAD_JQUERYUI:
    JS_URL.append(f"{JS_BASE_URL}jquery-ui-1.8.13.custom.min.js")

JS_URL.append(URL)

CSS_URL = []
if LOAD_JQUERYUI:
    CSS_URL.append(f"{CSS_BASE_URL}smoothness/jquery-ui-1.8.13.custom.css")

CSS_URL.extend(
    [f"{CSS_BASE_URL}elrte.full.css", f"{CSS_BASE_URL}django-elrte.css"]
)

ADMIN_FIELDS = getattr(settings, 'ELRTE_ADMIN_FIELDS', {})