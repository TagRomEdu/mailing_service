from django import template


register = template.Library()


@register.filter()
def mediapath(value):
    if value:
        return f'/static/media/{value}'
    return '/static/media/image_8.jpg'
