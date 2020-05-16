from django.urls import path
from . import views

app_name='posts' #cuz we used namespace in project urls.py


urlpatterns = [
    path('create_post',views.create_post,name='create_post'),
    path('',views.post_view,name='post_list'),
    path('like/',views.like_post,name='like_post'),
]