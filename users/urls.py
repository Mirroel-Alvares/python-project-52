from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersIndexView.as_view(), name='users_index'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    # path('<int:pk>/delete/', views.ArticleDelete.as_view(), name='delete'),
    # path('<int:pk>/update/', views.ArticleUpdate.as_view(), name='update'),
    # path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]
