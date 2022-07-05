from curses import def_prog_mode
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import board_app.models
import user_app.models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def board_main(request) :
    # 파라미터를 추출합니다.
    board_info_idx = request.GET['board_info_idx']

    # 현재 게시판 정보를 가져옵니다.
    board_model = board_app.models.BoardInfoTable.objects.get(board_info_idx=board_info_idx)

    template = loader.get_template('board_main.html')

    render_data = {
        'board_data' : board_model,
        'board_info_idx' : board_info_idx,
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
    template = loader.get_template('board_write.html')
    render_data = {

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

    message = '''
            <script>
                alert('저장되었습니다')
                locaiton.href = '/board/board_read'
            </script>
            '''
    return HttpResponse(message)