from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date():
    return datetime.today().strftime("%B %d, %Y")