from django import forms
from django.utils.encoding import smart_str
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

class CommaTags(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='text', name=name)
        objects = []
        for each in value:
            try:
                object = Tag.objects.get(pk=each)
            except:
                continue
            objects.append(object)

        values = []
        for each in objects:
            values.append(str(each))
        value = ', '.join(values)
        if value: # only add 'value' if it's nonempty
            final_attrs['value'] = force_unicode(value)
        return mark_safe(u'<input%s />' % flatatt(final_attrs))