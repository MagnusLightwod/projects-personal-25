from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # blank '' basically means default or home path.
    # should go here is you go to 127.0.0.1:8000

    # url pattern for post/post identifer
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]