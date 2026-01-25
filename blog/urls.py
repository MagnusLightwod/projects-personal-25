from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Posts listing moved to /posts/
    path('posts/', views.post_list, name='post_list'),

    # url pattern for post/post identifier
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
   # path ('', views.post_list, name='post_list'),
]