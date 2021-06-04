from django import template

register = template.Library()

@register.filter()
def format_name(value):
    names = value.split(" ")
    reversed_names = names[::-1]
    return ", ".join(reversed_names)
