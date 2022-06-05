from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import members.models

def index(request):
    template = loader.get_template('myfirst.html')

    # 데이터 베이스에 데이터 저장
    # 저장할 데이터를 가지고 있는 Model 객체를 생성합니다.
    model1 = members.models.Members(firstname = '홍', lastname = '길동')
    model2 = members.models.Members(firstname = '김', lastname = '길동')

    # 데이터 베이스에 저장
    # model1.save()
    # model2.save()
    
    # 조건절. 조건에 해당하는 로우가 다수일 경우
    # 특정 컬럼의 값이 지정된 값과 같을 경우
    query2 = members.models.Members.objects.filter(firstname = '홍')
    for q2 in query2:
        print(q2.firstname)

    # id 컬럼이 2보다 큰 것들을 가져옵니다.
    query3 = members.models.Members.objects.filter(id__gt = 2)
    for q3 in query3:
        print(q3.id)

    # 수정
    # 수정작업은 수정하고자 하는 행의 객체를 추출하고 값을 세팅한 다음에
    # save 함수를 호출합니다.
    query4 = members.models.Members.objects.get(id=3)
    # 값을 설정합니다.
    query4.firstname = '고'
    query4.lastname = '구려'
    # 저장 합니다.
    query4.save()

    # 삭제
    # 삭제 작업은 삭제하고자 하는 행의 객체를 추출하고
    # delete 함수를 호출합니다.
    # query5 = members.models.Members.objects.get(id=4)
    # query5.delete()

    PrintAll()

    # return HttpResponse(template.render())

    indexTemplate = loader.get_template('Index.html')
    title = "안녕하세요 Django 입니다"
    render_data = {
        'title' : title,
        'a200' : 5,
        'members' : query3,
    }

    return HttpResponse(indexTemplate.render(render_data, request))

def PrintAll():
    # 데이터 베이스의 모든 행을 가져옵니다.
    query1 = members.models.Members.objects.all()
    print(query1.values)

    # 각 데이터 출력
    for q1 in query1:
        print(q1.id)
        print(q1.firstname)
        print(q1.lastname)