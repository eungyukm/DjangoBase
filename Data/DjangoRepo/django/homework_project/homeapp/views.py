from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request) :

    render_data = {

    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(render_data, request))

def result(request) :

    # 데이터 베이스에 저장된 데이터를 불러온다.
    # pk를 기준으로 내림 차순 정렬한다.

    render_data = {
        # 읽어온 데이터를 셋팅해주고 html 에서 출력해준다.
    }

    template = loader.get_template('result.html')
    return HttpResponse(template.render(render_data, request))

@csrf_exempt
def add(request) :

    # 파라미터 데이터를 추출한다.

    # 데이터를 데이터베이스에 저장한다.

    r1 = '''
        <script>
            alert('작성이 완료되었습니다')
            location.href = '/result'
        </script>
         '''
    return HttpResponse(r1)
