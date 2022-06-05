import board_app.models

class TopMenuMiddleware :
    # 초기화 함수. 객체를 생성할 때 자동으로 호출되는 함수
    # django에서 미들웨어 객체를 생성할 때 다음 미들웨어 정보를
    # 두 번째 매개변수로 전달해준다.
    def __init__(self, next_layer=None) :
        self.get_response = next_layer

    # 요청정보 처리를 하기 위해 호출하는 함수
    # 데이터를 가져오거나 처리하는 작업
    def process_request(self, request) :
        # print('top menu middleware')

        # 데이터베이스에서 상단 메뉴를 구성하기 위해 필요한 데이터를 가져온다.
        menu_list = board_app.models.BoardInfoTable.objects.all()
        # request 영역에 저장한다.
        # print(menu_list)
        request.menu_list = menu_list

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