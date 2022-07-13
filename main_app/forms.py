from django.forms import ModelForm
from .models import Calendar

class Calendar(ModelForm):
  class Meta:
    model = Calendar
    fields = ['date']