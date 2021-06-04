from django import template 

register = template.Library()

@register.filter()
def split_name(value):
    return value.split(" ")