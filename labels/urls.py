from django.urls import path
from labels import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsIndexView.as_view(), name='labels_index'),
    path('create/', views.LabelCreate.as_view(), name='label_create'),
    path('<int:pk>/update/', views.LabelUpdate.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.LabelDelete.as_view(), name='label_delete'),
]
