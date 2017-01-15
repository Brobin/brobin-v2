from django import template
from fishing.models import Year


register = template.Library()


@register.inclusion_tag('fishing/tags/fishing_header.html', takes_context=True)
def fishing_year_buttons(context):
    years = Year.objects.all()
    return {'years': years, 'path': context['request'].path}
