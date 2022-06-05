from django.http import HttpResponse
import user_app.models
from django.shortcuts import redirect
from django.urls import resolve

class LoginCheckMiddleware :

    

    # 초기화 함수. 객체를 생성할 때 자동으로 호출되는 함수
    # django에서 미들웨어 객체를 생성할 때 다음 미들웨어 정보를
    # 두 번째 매개변수로 전달해준다.
    def __init__(self, next_layer=None) :
        self.get_response = next_layer

    # 요청정보 처리를 하기 위해 호출하는 함수
    # 데이터를 가져오거나 처리하는 작업
    def process_request(self, request) :
        
        # 검사를 하지 않을 페이지 주소
        except_list = [
            'index',        # 첫 페이지
            'join',         # 회원가입
            'login',        # 로그인
            'board_main',   # 게시글 목록
            'login_result', # 로그인 처리
            'join_result',  # 회원가입 처리
        ]        

        # 현재 페이지의 주소를 가져온다.
        now_name = resolve(request.path_info).url_name
        # print(now_name)

        # 제외 목록에 포함되어 있지 않을 경우
        if now_name not in except_list :
            # 로그인을 안했는지...
            if request.session.get('login_chk') != True :
                r1 = '''
                    <script>
                        alert('잘못된 접근 입니다')
                        location.href = '/'
                    </script>
                     '''
                return HttpResponse(r1)

    # 응답정보 처리를 하기 위해 호출하는 함수
    # 응답결과를 생성하는 작업을 수행. 요청 흐름을 통제하는 역할을 수행한다.
    def precess_response(self, request, response) :
        return response

    # django에서 미들웨어를 동작시킬 때 호출되는 함수
    def __call__(self, request) :
        response = self.process_request(request)

        if response is None :
            response = self.get_response(request)
        
        response = self.precess_response(request, response)
        return response