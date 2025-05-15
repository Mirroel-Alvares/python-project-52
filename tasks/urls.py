from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksIndexView.as_view(), name='tasks_index'),

]
