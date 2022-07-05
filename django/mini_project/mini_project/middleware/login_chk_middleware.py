from django.http import HttpResponse
from django.shortcuts import redirect

class LoginCheckMiddleware :

    def __init__(self, next_layer=None) :
        self.get_response = next_layer

    # 요청정보 처리를 하기위해 호출하는 함수
    def process_request(self, request) :
        pass

    # 응답정보를 처리하기 위해 호출하는 함수
    # 응답결과를 생성하는 작업을 수행. 요청 흐름을 통제하는 역할을 수행합니다.
    def precess_response(self, request, response) :
        # 검사를 하지 않을 페이지 주소
        except_list = [
            'index', # 첫 페이지
            'join', # 회원가입
            'login', # 로그인
            'board_main', # 게시글 목록
            'logout', # 로그아웃
        ]

        # 현재 페이지의 주소를 가져옵니다.
        now_name = request.resolver_match.url_name
        print(now_name)

        # 제외 목록에 포함되어 있는 경우
        if now_name in except_list:
            return response
        # 제외 목록에 포함되어 있지 않는 경우
        else :
            # 로그인을 했는지 체크
            if request.session.get('login_chk') == True:
                return response
            else :
                message = '''
                        <script>
                            alert('잘못된 접근 입니다.')
                            location.href = '/'
                        </script>
                        '''
                return HttpResponse(message)

    # 장고에서 미들웨어르 동작시킬 때 호출하는 함수
    def __call__(self, request) :
        response = self.process_request(request)

        if response is None :
            response = self.get_response(request)

        response = self.precess_response(request, response)
        return response