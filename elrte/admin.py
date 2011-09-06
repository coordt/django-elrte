from django.db.models import get_model
from django.contrib import admin
from django import forms
from django.core.exceptions import ImproperlyConfigured

from widgets import AdminElrteTextareaWidget

from elrte import settings
REGISTRY = {}

for key, val in settings.ADMIN_FIELDS.items():
    if not isinstance(key, basestring):
        raise ImproperlyConfigured("Please specify the ELRTE_ADMIN_FIELDS models using a string.")
    
    REGISTRY[get_model(*key.split('.'))] = val

class ElrteAdmin(admin.ModelAdmin):
    editor_fields = ()
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.editor_fields:
            return db_field.formfield(widget=AdminElrteTextareaWidget())
        return super(ElrteAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        
for model,modeladmin in admin.site._registry.items():
    if model in REGISTRY:
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (ElrteAdmin, modeladmin.__class__), {
            'editor_fields': REGISTRY[model],
        }))