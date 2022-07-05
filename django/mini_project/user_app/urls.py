from django.urls import path
from . import views


urlpatterns = [
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('modify_user', views.modify_user, name='modify_user'),
    path('join_result', views.join_result, name='join_result'),
    path('login_result', views.login_result, name='login_result'),
    path('logout', views.logout, name='logout'),
    path('modify_user_result', views.modify_user_result, name='modify_user_result'),
]