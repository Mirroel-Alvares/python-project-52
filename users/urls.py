from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersIndexView.as_view(), name='users_index'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    # path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]
