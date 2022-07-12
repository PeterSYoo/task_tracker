from django.urls import path
from . import views

from .timer import start_timer, stop_timer, discard_timer

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tasks/', views.tasks_index, name='tasks_index'),
  path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
  path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
  path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
  path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),

  path('accounts/signup/', views.signup, name='signup'),

  # Timer
  path('api/start_timer/', start_timer, name='start_timer'),
  path('api/stop_timer/', stop_timer, name='stop_timer'),
  path('api/discard_timer/', discard_timer, name='discard_timer'),
]