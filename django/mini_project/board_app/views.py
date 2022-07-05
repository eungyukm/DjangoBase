from curses import def_prog_mode
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import board_app.models
import user_app.models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def board_main(request) :
    # 파라미터를 추출합니다.
    board_info_idx = request.GET['board_info_idx']

    page_num = request.GET.get('page_num')
    if page_num == None :
        page_num = '1'

    page_num = int(page_num)

    # 현재 게시판 정보를 가져옵니다.
    board_model = board_app.models.BoardInfoTable.objects.get(board_info_idx=board_info_idx)

    # 현재 게시판의 글 목록을 가져옵니다.
    content_list = board_app.models.ContentTable.objects
    content_list = content_list.select_related('content_writer_idx' , 'content_board_idx')
    content_list = content_list.filter(content_board_idx = board_info_idx)
    content_list = content_list.order_by('-content_idx')

    # 페이징을 위한 객체를 생성합니다.
    # 첫 번째 : 전체 데이터 목록,
    # 두 번째 : 한 페이지당 보여줄 데이터의 개수
    paginator = Paginator(content_list, 10)
    content_list = paginator.get_page(page_num)

    template = loader.get_template('board_main.html')

    render_data = {
        'board_data' : board_model,
        'board_info_idx' : board_info_idx,
        'content_list' : content_list,
        'pagenation_data' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return HttpResponse(template.render(render_data, request))

# board/board_modify
def board_modify(request) :
    template = loader.get_template('board_modify.html')
    render_data = {

    }
    return HttpResponse(template.render(render_data, request))

# board/board_read
def board_read(request):

    # 파라미터 데티어를 추출
    board_info_idx = request.GET['board_info_idx']
    print(board_info_idx)
    content_idx = request.GET['content_idx']
    print(content_idx)

    # 현재 글 정보를 가져옵니다.
    # 외래키 관계로 묶여 있으므로 select_related 함수를 사용합니다.
    content_model = board_app.models.ContentTable.objects.select_related('content_writer_idx', 'content_board_idx').get(content_idx=content_idx)
    print(content_model.content_writer_idx.user_name)


    template = loader.get_template('board_read.html')
    render_data = {
        'content_data' : content_model,
        'board_info_idx' : board_info_idx,
        'content_idx' : content_idx
    }
    return HttpResponse(template.render(render_data, request))

# board/board_write
def board_write(request):
    # 파라미터를 추출합니다.
    board_info_idx = request.GET['board_info_idx']

    template = loader.get_template('board_write.html')
    render_data = {
        'board_info_idx' : board_info_idx
    }
    return HttpResponse(template.render(render_data, request))


@csrf_exempt
def board_write_result(request) :
    content_subject = request.POST['board_subject']
    content_text = request.POST['board_content']
    content_date = timezone.localtime()

    content_writer_idx = request.session['login_user_idx']
    # 외래키(BoardInfoTable의 PK 컬럼을 참조한다)
    content_board_idx = request.POST['board_info_idx']

    content_model = board_app.models.ContentTable()
    content_model.content_subject = content_subject
    content_model.content_text = content_text
    content_model.content_date = content_date

    content_writer_model = user_app.models.UserTable.objects.get(user_idx=content_writer_idx)
    content_board_model = board_app.models.BoardInfoTable.objects.get(board_info_idx = content_board_idx)

    content_model.content_writer_idx = content_writer_model
    content_model.content_board_idx = content_board_model

    # 업로드된 파일 명을 가져옵니다.
    content_model.content_file = request.FILES.get('board_file')

    content_model.save()

    content_model2 = board_app.models.ContentTable.objects.all().order_by('-content_idx')[0]
    # print(content_model2.content_idx)
    # 정렬한 데이터의 가장 최근 데이터로 정렬한다.

    message = f'''
            <script>
                alert('저장되었습니다')
                locaiton.href = '/board/board_read?board_info_idx={content_board_idx}&content_idx={content_model2.content_idx}'
            </script>
            '''
    return HttpResponse(message)