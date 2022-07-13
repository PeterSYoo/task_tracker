from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('tasks/', views.tasks_index, name='tasks_index'),
  path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
  path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
  path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
  path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
  path('tasks/<int:task_id>/add_date/', views.add_date, name='add_date'),
  path('tasks/<int:task_id>/assoc_users/<int:users_id>/', views.assoc_users, name='assoc_users'),
  path('tasks/<int:task_id>/add_photo/', views.add_photo, name='add_photo'),

  path('accounts/signup/', views.signup, name='signup'),
]