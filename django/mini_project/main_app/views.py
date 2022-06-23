from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import board_app.models

# Create your views here.
def index(request):
    # board_info_table에 기본 데이터 저장
    # 한번 수행 후 주석처리 해주세요~
    # model1 = board_app.models.BoardInfoTable()
    # model1.board_info_name = "자유게시판"
    # model1.save()

    # model2 = board_app.models.BoardInfoTable()
    # model2.board_info_name = "유머게시판"
    # model2.save()

    # model3 = board_app.models.BoardInfoTable()
    # model3.board_info_name = "정치게시판"
    # model3.save()

    # model4 = board_app.models.BoardInfoTable()
    # model4.board_info_name = "스포츠게시판"
    # model4.save()

    template = loader.get_template('index.html')
    return HttpResponse(template.render())  