from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksIndexView.as_view(), name='tasks_index'),
    path('create/', views.TasksCreate.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TasksUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TasksDelete.as_view(), name='task_delete'),
    path('<int:pk>/', views.TasksDetails.as_view(), name='task_details'),
]
