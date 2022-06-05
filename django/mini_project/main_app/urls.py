from django.urls import path
from . import views

urlpatterns = [
    # 주소만 입력했을 경우 (main 페이지)
    path('', views.index, name='index'),
]