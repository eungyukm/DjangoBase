import board_app.models

class TopMenuMiddleware : 
    # 초기화 함수
    # django에서 미들웨어 객체를 생성할 때 다음 미들에어 정보를
    # 두번 째 매개변수로 전달해줍니다.
    def __init__(self, next_layer=None) :
        self.get_response = next_layer

    # 요청정보 처리를 하기위해 호출하는 함수
    def process_request(self, request) :
        # print('top menu middleware')
        # 데이터베이스에서 상단 메뉴를 구성하기 위해 필요한 데이터를 가져옵니다.
        menu_list = board_app.models.BoardInfoTable.objects.all()
        
        # print(menu_list)
        # request 영역에 저장합니다.
        request.menu_list = menu_list


    # 응답정보를 처리하기 위해 호출하는 함수
    # 응답결과를 생성하는 작업을 수행. 요청 흐름을 통제하는 역할을 수행합니다.
    def precess_response(self, request, response) :
        return response

    # 장고에서 미들웨어르 동작시킬 때 호출하는 함수
    def __call__(self, request) :
        response = self.process_request(request)

        if response is None :
            response = self.get_response(request)

        response = self.precess_response(request, response)
        return response