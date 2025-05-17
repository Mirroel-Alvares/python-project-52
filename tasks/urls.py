from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksIndexView.as_view(), name='tasks_index'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('<int:pk>/', views.TaskDetails.as_view(), name='task_details'),
]
