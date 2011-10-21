from django import template
register = template.Library()

from btc_app.models import *

@register.inclusion_tag('btc_app/templates/blogroll.html')
def get_blogRolls():
    """Return the blog roll"""
    return {'blogs': blogRoll.objects.all()}