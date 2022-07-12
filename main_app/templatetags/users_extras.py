from django import template
from ..models import Task

register = template.Library()

@register.simple_tag
def get_username_from_userid(user_id):
  try:
    return Task.objects.get(id=user_id).get_username()
  except Task.DoesNotExist:
    return 'Unknown'