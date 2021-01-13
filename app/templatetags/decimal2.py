from django import template

register = template.Library()

@register.filter
def decimal(value):
    try:
        return "%.2f" % value
    except:
        pass