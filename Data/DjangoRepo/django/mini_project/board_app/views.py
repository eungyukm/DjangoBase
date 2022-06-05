from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import board_app.models
import user_app.models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
# board/board_main
def board_main(request) :

    # 파라미터를 추출한다.
    board_info_idx = request.GET['board_info_idx']

    page_num = request.GET.get('page_num')
    if page_num == None :
        page_num = '1'

    page_num = int(page_num)

    # 현재 게시판 정보를 가져온다
    board_model = board_app.models.BoardInfoTable.objects.get(board_info_idx=board_info_idx)   

    # 현재 게시판의 글 목록을 가져온다
    content_list = board_app.models.ContentTable.objects
    content_list = content_list.select_related('content_writer_idx', 'content_board_idx')
    content_list = content_list.filter(content_board_idx = board_info_idx)
    content_list = content_list.order_by('-content_idx')

    # 전체 글의 개수를 가져온다.
    content_cnt = len(content_list)

    # 페이징을 위한 객체를 생성한다.
    # 첫 번째 : 전체 데이터 목록, 두 번째 : 한 페이지당 보여줄 데이터의 개수
    paginator = Paginator(content_list, 10)
    # 현재 페이지의 데이터 목록을 가져온다.
    content_list = paginator.get_page(page_num)


    # 하단 페이지네이션의 최소와 최대 값을 구한다.
    a1 = int((page_num - 1) / 10)
    a2 = a1 * 10
    page_min = a2 + 1
    page_max = page_min + 9
    
    # 전체 페이지 수를 구한다.
    page_cnt = content_cnt // 10
    if content_cnt % 10 > 0 :
        page_cnt = page_cnt + 1

    # 만약 page_max가 전체 페이지 수 보다 크다면 전체 페이지수로 셋팅한다.
    if page_max > page_cnt :
        page_max = page_cnt
    
    # 이전
    page_prev = page_min - 1
    # 다음
    page_next = page_max + 1

    # page_next가 page_cnt보다 크면 전체 페이지수로 셋팅한다.
    if page_next > page_cnt :
        page_next = page_cnt

    pagenation_list = list(range(page_min, page_max + 1))

    template = loader.get_template('board_main.html')

    render_data = {
        'board_data' : board_model,
        'board_info_idx' : board_info_idx,
        'content_list' : content_list,
        'pagenation_data' : pagenation_list,
        'page_num' : page_num,
        'page_prev' : page_prev,
        'page_next' : page_next,
        'page_cnt' : page_cnt,
    }

    return HttpResponse(template.render(render_data, request))

# board/board_modify
def board_modify(request) :

    # 파라미터 데이터를 추출한다.
    board_info_idx = request.GET['board_info_idx']
    content_idx = request.GET['content_idx']
    page_num = request.GET['page_num']

    # 현재 글 정보를 가져온다.
    content_model = board_app.models.ContentTable.objects
    content_model = content_model.select_related('content_writer_idx', 'content_board_idx')
    content_model = content_model.get(content_idx=content_idx)

    template = loader.get_template('board_modify.html')
    
    render_data = {
        'board_info_idx' : board_info_idx,
        'content_idx' : content_idx,
        'page_num' : page_num,
        'content_model' : content_model,
    }

    return HttpResponse(template.render(render_data, request))

# board/board_read
def board_read(request) :

    # 파라미터 데이터를 추출한다.
    board_info_idx = request.GET['board_info_idx']
    content_idx = request.GET['content_idx']
    page_num = request.GET['page_num']

    # 현재 글 정보를 가져온다.
    # 외래키 관계로 설정되어 있는 것이 있다면
    # select_related 함수를 사용한다.
    # 이 함수 안에는 외래키 관계로 설정되어 있는 컬럼의 이름을 작성해준다.
    # content_model = board_app.models.ContentTable.objects.select_related('content_writer_idx', 'content_board_idx').get(content_idx=content_idx)
    content_model = board_app.models.ContentTable.objects
    content_model = content_model.select_related('content_writer_idx', 'content_board_idx')
    content_model = content_model.get(content_idx=content_idx)

    # print(content_model.content_idx)
    # print(content_model.content_writer_idx.user_idx)
    # print(content_model.content_board_idx.board_info_idx)


    template = loader.get_template('board_read.html')

    render_data = {
        'content_data' : content_model,
        'board_info_idx' : board_info_idx,
        'content_idx' : content_idx,
        'page_num' : page_num,
    }

    return HttpResponse(template.render(render_data, request))

# board/board_write
def board_write(request) :

    # 파라미터 추출한다.
    board_info_idx = request.GET['board_info_idx']

    template = loader.get_template('board_write.html')
    
    render_data = {
        'board_info_idx' : board_info_idx
    }

    return HttpResponse(template.render(render_data, request))

# /board/board_write_result
@csrf_exempt
def board_write_result(request) :

    # 파라미터 데이터 추출
    content_subject = request.POST['board_subject']
    content_text = request.POST['board_content']
    content_date = timezone.localtime()
    content_writer_idx = request.session['login_user_idx']
    content_board_idx = request.POST['board_info_idx']

    
    # 저장한다.
    content_model = board_app.models.ContentTable()
    content_model.content_subject = content_subject
    content_model.content_text = content_text
    content_model.content_date = content_date

    # 외래키 관계로 설정되어 있는 것은 참조하는 모델의 객체를 설정해줘야 한다.
    content_writer_model = user_app.models.UserTable.objects.get(user_idx=content_writer_idx)
    content_board_model = board_app.models.BoardInfoTable.objects.get(board_info_idx=content_board_idx)

    content_model.content_writer_idx = content_writer_model
    content_model.content_board_idx = content_board_model

    # 업로드된 파일 명을 가져온다.
    content_model.content_file = request.FILES.get('board_file')

    content_model.save()

    # 글 번호를 기준으로 내림 차순 정렬한다.
    # 컬럼명만 적어주면 오름 차순 정렬이고 컬럼명에 - 를 붙혀주면 내림 차순
    # 정렬이 된다.
    content_model2 = board_app.models.ContentTable.objects.all().order_by('-content_idx')[0]
    # print(content_model2.content_idx)

    r1 = f'''
        <script>
            alert('저장되었습니다')
            location.href = '/board/board_read?board_info_idx={content_board_idx}&content_idx={content_model2.content_idx}&page_num=1'
        </script>
         '''

    return HttpResponse(r1)


# /board/board_delete
def board_delete(request) :

    # 파라미터 데이터를 추출한다.
    board_info_idx = request.GET['board_info_idx']
    content_idx = request.GET['content_idx']

    # 글을 삭제한다.
    content_model = board_app.models.ContentTable.objects.get(content_idx=content_idx)
    content_model.delete()

    r1 = f'''
        <script>
            alert('삭제되었습니다')
            location.href = '/board/board_main?board_info_idx={board_info_idx}'
        </script>
         '''

    return HttpResponse(r1)


# /board/board_modify_result
@csrf_exempt
def board_modify_result(request) :

    # 파라미터 추출
    board_info_idx = request.POST['board_info_idx']
    content_idx = request.POST['content_idx']
    page_num = request.POST['page_num']
    content_subject = request.POST['board_subject']
    content_text = request.POST['board_content']
    
    content_file = request.FILES.get('board_file')

    
    
    # print(content_file)

    # 수정하고자 하는 글 정보를 가져온다.
    content_model = board_app.models.ContentTable.objects.get(content_idx=content_idx)

    # 정보를 셋팅한다.
    content_model.content_subject = content_subject
    content_model.content_text = content_text

    if content_file :
        content_model.content_file = content_file

    # 저장한다.
    content_model.save()

    r1 = f'''
        <script>
            alert('수정되었습니다')
            location.href = '/board/board_modify?board_info_idx={board_info_idx}&page_num={page_num}&content_idx={content_idx}'
        </script>
          '''

    return HttpResponse(r1)