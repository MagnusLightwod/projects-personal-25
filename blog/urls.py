from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.post_list, name='post_list'),
    # should go here is you go to 127.0.0.1:8000

]