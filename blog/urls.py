from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='home'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('comments/<int:pk>/', views.comment_thread, name='comment_thread'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<category>', views.blog_category, name="blog_category"),
]