from django.contrib import admin
from .models import Task, Calendar, Photo

# Register your models here.
admin.site.register(Task)
admin.site.register(Calendar)
admin.site.register(Photo)