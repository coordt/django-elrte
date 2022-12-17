from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt
from django.forms.util import force_unicode
from django.utils.html import escape
from django.utils import simplejson
from django.utils.datastructures import SortedDict
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _
from django.template.loader import render_to_string

import elrte.settings

ELRTE_DEFAULT_OPTIONS = {
    'doctype': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">',
    'cssClass': 'el-rte',
    'cssfiles': [f'{elrte.settings.CSS_BASE_URL}elrte-inner.css'],
    'absoluteURLs': True,
    'allowSource': True,
    'lang': 'en',
    'styleWithCss': False,
    'height': None,
    'fmAllow': True,
    'toolbar': 'normal',
}

ELRTE_LANG_INCLUSION = (
    f"i18n/elrte.{getattr(ELRTE_DEFAULT_OPTIONS, 'lang', 'en')}.js"
)


class FileManagerOpener(object):
    """An abstract way to handle the javascript call to open a file manager"""
    def __init__(self, arg):
        super(FileManagerOpener, self).__init__()
        # Use the {{ adminmedia }}js/admin/RelatedObjectLookups.js
        #
    def get_javascript():
        """
        Render the template for the finction
        """
        """function(callback) {}"""


class ElrteTextareaWidget(forms.Textarea):
    """
    A textarea widget that uses elRTE for a Rich Text Editor on a textarea
    """
    
    def __init__(self, attrs=None):
        super(ElrteTextareaWidget, self).__init__(attrs)
    
    def get_config(self, name):
        """
        Render the config template into a string
        """
        options = ELRTE_DEFAULT_OPTIONS.copy()
        options.update(getattr(settings, 'ELRTE_OPTIONS', {}))
        for key, val in options.items():
            options[key] = simplejson.dumps(val)
        return render_to_string("elrte/config.html", {'options': options, 'name':name})
        
    
    def render(self, name, value, attrs=None):
        value = value or u''
        value = force_unicode(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name
        config = self.get_config(name)
        html = [f'<textarea{flatatt(final_attrs)}>{escape(value)}</textarea>']
        html.append(u'<input type="hidden" name="%(name)s_img" id="%(name)s_img">' % {'name': name})
        html.append(config)
        return mark_safe(u'\n'.join(html))

    def _media(self):
        js = elrte.settings.JS_URL
        css = {'all': elrte.settings.CSS_URL}
        try:
            result = forms.Media(js=js, css=css)
        except Exception, e:
            print e
        print result
        return result
    media = property(_media)


class AdminElrteTextareaWidget(ElrteTextareaWidget, admin_widgets.AdminTextareaWidget):
    pass


def get_language_config(content_language=None):
    language = get_language()[:2]
    content_language = content_language[:2] if content_language else language
    config = {'language': language}
    lang_names = SortedDict()
    for lang, name in settings.LANGUAGES:
        if lang[:2] not in lang_names: lang_names[lang[:2]] = []
        lang_names[lang[:2]].append(_(name))
    sp_langs = []
    for lang, names in lang_names.items():
        default = '+' if lang == content_language else ''
        sp_langs.append(f"{default}{' / '.join(names)}={lang}")

    config['spellchecker_languages'] = ','.join(sp_langs)

    if content_language in settings.LANGUAGES_BIDI:
        config['directionality'] = 'rtl'
    else:
        config['directionality'] = 'ltr'

#    TODO: Not implemented
#    if elrte.settings.USE_SPELLCHECKER:
#        config['spellchecker_rpc_url'] = reverse('elrte.views.spell_check')

    return config
