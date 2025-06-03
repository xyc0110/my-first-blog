from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 文章列表页
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 文章详情页
]
