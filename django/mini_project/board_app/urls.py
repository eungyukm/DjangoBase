from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('board_main', views.board_main, name='board_main'),
    path('board_modify', views.board_main, name='board_modify'),
    path('board_read', views.board_main, name='board_read'),
    path('board_write', views.board_write, name='board_write'),
    path('board_write_result', views.board_write_result, name='board_write_result'),
]