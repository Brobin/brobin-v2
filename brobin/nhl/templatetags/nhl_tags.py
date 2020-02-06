from django import template


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def percent(value, arg):
    if arg == 0:
        return '---'
    return '{0:.1f}%'.format(value / arg * 100)
