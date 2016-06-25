from django import template
from fishing.models import Year


register = template.Library()


@register.inclusion_tag('fishing/tags/fishing_header.html')
def fishing_year_buttons():
    years = Year.objects.all()
    return {'years': years}
