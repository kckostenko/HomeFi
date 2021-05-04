from django import template

register = template.Library()

@register.simple_tag
def update_variable(value):
    #Now can update existing var in templates
    return value