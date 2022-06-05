from django.urls import path
from . import views

# 요청될 함수를 주소와 매핑한다.
urlpatterns = [
    # '' : 요청시 사용한 주소. '' 는 생략했을 경우
    # views.index : 요청이 발생했을 때 호출될 함수
    # name='index' : 요청에 대한 관리 이름. 생략해도 됩니다.
    path('', views.index, name='index'),
    path('test1', views.test1, name='test1')
]