from django import template
from django.conf import settings
import os
register = template.Library()

from btc_app.models import *

@register.inclusion_tag(os.path.join(settings.SITE_ROOT,'btc_app/templates/blogroll.html'))
def get_blogRolls():
    """Return the blog roll"""
    return {'blogs': blogRoll.objects.all()}