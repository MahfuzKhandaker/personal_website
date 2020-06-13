from django import template
from ..models import Post

register = template.Library()


@register.inclusion_tag('_latest_posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1)[:3]
    return {'posts': posts}