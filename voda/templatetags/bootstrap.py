from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def class_active(context, url_name=None):
    request = context['request']
    if request.path == reverse(url_name):
        return 'class=active'
    else:
        return ''
