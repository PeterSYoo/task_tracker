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

  def date_for_today(self):
    return self.calendar_set.filter(date=date.today()).count()

class Calendar(models.Model):
  date = models.DateField('date')
  task = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for task_id: {self.task_id} @{self.url}"