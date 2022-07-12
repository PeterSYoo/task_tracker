from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  users_tasks = Task.objects.filter(users=request.user)
  user_tasks = Task.objects.filter(user=request.user)
  return render(request, 'tasks/index.html', { 
    'users_tasks': users_tasks,
    'user_tasks': user_tasks,
    })

def tasks_detail(request, task_id):
  tasks = Task.objects.get(id=task_id)
  users = tasks.users.all()
  user = User.objects.all()
  users_task_doesnt_have = User.objects.exclude(id__in=tasks.users.all().values_list('id'))
  # exclude objects in users query that have primary keys in this list [1, 4, 5, etc.]

  return render(request, 'tasks/details.html', { 
    'tasks': tasks,
    'users': users,
    'user': user,
    'add_users': users_task_doesnt_have,
    })

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

class TaskCreate(CreateView):
  model = Task
  fields = ['name', 'description']
  success_url = '/tasks/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(UpdateView):
  model = Task
  fields = ['name', 'description']

class TaskDelete(DeleteView):
  model = Task
  success_url = '/tasks/'