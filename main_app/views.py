from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Task, Photo
from .forms import Calendar
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'tasktracker-py'

# Create your views here.
def home(request):
  return render(request, 'home.html')

@login_required
def tasks_index(request):
  users_tasks = Task.objects.filter(users=request.user)
  user_tasks = Task.objects.filter(user=request.user)
  calendar = Calendar()
  return render(request, 'tasks/index.html', { 
    'users_tasks': users_tasks,
    'user_tasks': user_tasks,
    'calendar': calendar,
    })

@login_required
def tasks_detail(request, task_id):
  tasks = Task.objects.get(id=task_id)
  users = tasks.users.all()
  user = User.objects.all()
  users_task_doesnt_have = User.objects.exclude(id__in=tasks.users.all().values_list('id'))
  # exclude objects in users query that have primary keys in this list [1, 4, 5, etc.]
  calendar = Calendar()
  return render(request, 'tasks/details.html', { 
    'tasks': tasks,
    'users': users,
    'user': user,
    'calendar': calendar,
    'add_users': users_task_doesnt_have,
    })

def add_date(request, task_id):
  # create the ModelForm using the data in request.POST
  form = Calendar(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the task_id assigned
    new_date = form.save(commit=False)
    new_date.task_id = task_id
    new_date.save()
  return redirect('detail', task_id=task_id)

@login_required
def assoc_users(request, task_id, users_id):
  Task.objects.get(id=task_id).users.add(users_id)
  return redirect('detail', task_id=task_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('tasks_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def add_photo(request, task_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to task_id or task (if you have a task object)
            photo = Photo(url=url, task_id=task_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', task_id=task_id)

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['name', 'description']
  success_url = '/tasks/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['name', 'description']

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  success_url = '/tasks/'