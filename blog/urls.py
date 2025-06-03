from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 文章列表页
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 文章详情页
    path('post/new/', views.post_new, name='post_new'),  # 新建文章页
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # 编辑文章页（新增）
]

