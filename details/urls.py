from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('friendlist/', views.friend_list, name="friendlist"),
    path('newfriends/', views.potential_friends, name="newfriends"),
    path('profilepage/<str:pk>/', views.profile_page, name="profilepage"),
    path('sendrequest/<str:pk>/', views.send_request, name="sendrequest"),
    path('friendrequest/', views.friend_request, name="friendrequest"),

]