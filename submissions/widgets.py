from django import forms
from django.utils.encoding import smart_str
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from submissions.models import Tag, Submission

class CommaTags(forms.Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='text', name=name)
        if not type(value) == unicode:
            values = []
            for each in value:
                try:
                    values.append(str(Tag.objects.get(pk=each).name))
                except:
                    continue
            value = ', '.join(values)
            if value: # only add 'value' if it's nonempty
                final_attrs['value'] = smart_str(value)
        else:
            final_attrs['value'] = smart_str(value)
        return mark_safe(u'<input%s />' % flatatt(final_attrs))