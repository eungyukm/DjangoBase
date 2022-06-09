from django.urls import path
from . import views


urlpatterns = [
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('modify_user', views.modify_user, name='modify_user')
]