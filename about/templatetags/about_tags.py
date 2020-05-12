from django import template
from about.models import About

register = template.Library()


@register.inclusion_tag('_about_me.html')
def about_me():
    abouts = About.objects.all()
    return {'abouts': abouts}

@register.inclusion_tag('_about_me_detail.html')
def about_me_detail():
    abouts = About.objects.all()
    return {'abouts': abouts}