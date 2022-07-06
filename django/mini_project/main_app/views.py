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

    # 게시판 정보를 가져옵니다.
    board_list = board_app.models.BoardInfoTable.objects.all()

    # 각 게시판별 게시글 상위 5개를 담을 리스트
    content_list = []

    # 게시판의 수 만큼 반복합니다.
    for b1 in board_list :
        # 현재 게시판에서 상위글 5개를 가져옵니다.
        c1 = board_app.models.ContentTable.objects.all().filter(content_board_idx=b1.board_info_idx)
        c1 = c1.order_by('-content_idx')[:5]
        content_list.append(c1)

        # 게시판 정보와 게시글 정보를 하나로 묶어 준다.
        board_data_list = zip(board_list, content_list)

    render_data = {
        'board_list' : board_list,
        'content_list' : content_list,
        'board_data_list' : board_data_list,
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(render_data, request))