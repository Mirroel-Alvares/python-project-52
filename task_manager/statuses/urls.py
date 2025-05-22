from django.urls import path
from task_manager.statuses import views

app_name = 'statuses'

urlpatterns = [
    path('', views.StatusesIndexView.as_view(), name='statuses_index'),
    path('create/', views.StatusCreate.as_view(), name='status_create'),
    path(
        '<int:pk>/update/',
        views.StatusUpdate.as_view(),
        name='status_update'
    ),
    path(
        '<int:pk>/delete/',
        views.StatusDelete.as_view(),
        name='status_delete'
    ),
]
