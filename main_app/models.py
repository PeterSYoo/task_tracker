from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  users = models.ManyToManyField(User, related_name='tasks_set')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'task_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return 