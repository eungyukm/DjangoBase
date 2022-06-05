from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import members.models

# Create your views here.
# 요청이 발생했을 때 호출되는 함수
# 요청 하나당 하나씩 만들어준다.

# 이 함수가 호출될 주소는 urls.py 파일에 매핑되어 있다.
def index(request) :
    # 브라우저로 보낼 응답 결과를 생성해 반환한다.
    # html 파일 데이터를 읽어온다.
    html = loader.get_template('index.html')

    # 데이터 베이스에 데이터 저장
    # 저장할 데이터를 가지고 있는 Model 객체를 생성한다.
    # model1 = members.models.Members(first_name='홍', last_name='길동')
    # model2 = members.models.Members(first_name='김', last_name='길동')
    # model3 = members.models.Members(first_name='최', last_name='길동')
    # model4 = members.models.Members(first_name='박', last_name='길동')
    # model5 = members.models.Members(first_name='고', last_name='길동')

    # # 데이터 베이스에 저장한다.
    # # Model 객체를 새롭게 생성해서 save 함수를 호출하면 insert가 된다.
    # model1.save()
    # model2.save()
    # model3.save()
    # model4.save()
    # model5.save()

    # 데이터베이스에 저장된 데이터 모두를 가져온다.
    # 모든 행, 모든 컬럼
    # member_list = members.models.Members.objects.all()
    # print(member_list.values())

    # for m1 in member_list :
    #     print(m1.id)
    #     print(m1.first_name)
    #     print(m1.last_name)
    #     print('-------------------------')

    # 모든 행, 특정 컬럼
    # member_list = members.models.Members.objects.only('id', 'first_name')

    # for m1 in member_list :
    #     print(m1.id)
    #     print(m1.first_name)
    #     print('--------------------------------')

    # 조건절. 조건에 해당하는 로우가 다수일 경우
    # 특정 컬럼의 값이 지정된 값과 같을 경우
    member_list = members.models.Members.objects.filter(first_name = '홍')
    # 그 외의 조건 키워드
    # https://velog.io/@dnpxm387/TIL-django-query-%EC%A1%B0%EA%B1%B4-%ED%82%A4%EC%9B%8C%EB%93%9C
    # 컬럼명__키워드 형태로 작성한다.

    # id 컬럼이 2보다 큰 것들을 가져온다.
    # member_list = members.models.Members.objects.filter(id__gt = 2)
    # print(member_list.query)

    # for m1 in member_list :
    #     print(m1.id)
    #     print(m1.first_name)
    #     print(m1.last_name)
    #     print('------------------------------')

    # 조건에 맞는 행이 하나인 경우. 조건은 filter에서 사용한 것과 동일하게 작업을 해준다.
    # member1 = members.models.Members.objects.get(id=1)
    # print(member1.id)
    # print(member1.first_name)
    # print(member1.last_name)

    # 수정
    # 수정작업은 수정하고자 하는 행의 객체를 추출하고 값을 셋팅한 다음에
    # save 함수를 호출해 준다.
    # member3 = members.models.Members.objects.get(id=3)
    # # 값을 설정한다.
    # member3.first_name = '이'
    # member3.last_name = '순신'
    # # 저장한다.
    # member3.save()

    # 삭제
    # 삭제 작업은 삭제하고자 하는 행의 객체를 추출하고
    # delete 함수를 호출해준다.
    # member3 = members.models.Members.objects.get(id=3)
    # member3.delete()


    # member_list = members.models.Members.objects.all()

    # for m1 in member_list :
    #     print(m1.id)
    #     print(m1.first_name)
    #     print(m1.last_name)
    #     print('--------------------------------')


    # return HttpResponse("Hello World")
    # html 데이터를 이용해 응답 결과를 생성하여 브라우저로 전달한다.

    member_list = members.models.Members.objects.all()

    # html을 렌더링 하기 위해 필요한 데이터
    render_data = {
        'title' : '안녕하세요',
        'a200' : 5,
        'member_list' : member_list,
    }

    return HttpResponse(html.render(render_data, request))

def test1(request) :
    return HttpResponse("test")
