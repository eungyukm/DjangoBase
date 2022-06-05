from tempfile import tempdir
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import user_app.models

# Create your views here.

# user/join
def join(request) :
    template = loader.get_template('join.html')

    render_data = {

    }

    return HttpResponse(template.render(render_data, request))

# user/login
def login(request) :

    # 로그인 확인 여부를 나타나는 파라미터를 추출한다.
    # 지정된 파라미터가 없을 수도 있다면 get 함수를 사용한다.
    login_chk = request.GET.get('login_chk')
    # print(login_chk)

    render_data = {
        'login_chk' : login_chk
    }

    template = loader.get_template('login.html')
    return HttpResponse(template.render(render_data, request))

# user/modify_user
def modify_user(request) :

    # 로그인한 사용자의 정보를 가져온다.
    login_user_idx = request.session['login_user_idx']
    login_user_model = user_app.models.UserTable.objects.get(user_idx=login_user_idx)
    # print(login_user_model)

    render_data = {
        'login_user_data' : login_user_model
    }

    template = loader.get_template('modify_user.html')
    return HttpResponse(template.render(render_data, request))

# user/join_result
# post 요청시에는 csrf 토큰을 사용하게 된다.
# 이럴 경후 함수에 csrf_exempt 라는 데코레이션을 설정해줘야 한다.
@csrf_exempt
def join_result(request) :

    # print(request.POST['user_name'])
    # print(request.POST['user_id'])
    # print(request.POST['user_pw'])

    # 파라미터 데이터를 추출한다.
    user_name = request.POST['user_name']
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']

    # 저장처리
    user_model = user_app.models.UserTable()
    user_model.user_name = user_name
    user_model.user_id = user_id
    user_model.user_pw = user_pw
    user_model.save()

    r1 = '''
        <script>
            alert('가입이 완료되었습니다')
            location.href = '/user/login'
        </script>
         '''

    return HttpResponse(r1)

# /user/login_result
@csrf_exempt
def login_result(request) :

    # 사용자가 입력한 파라미터를 추출한다.
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    # print(user_id)
    # print(user_pw)

    # 데이터베이스에서 사용자 데이터를 가져온다.
    # 데이터를 가져올 때 조건에 만족하는 것이 없으면 오류가 발생한다.
    # 데이터가 없을 때의 처리를 해야 한다면 예외처리를 통해 처리한다.
    try :
        user_model = user_app.models.UserTable.objects.get(user_id = user_id)
        # print(user_model)

        # 로그인한 사용자와 데이터베이스에서 가져온 데이터의 비밀번호가 같을 경우
        if user_pw == user_model.user_pw :

            # 로그인에 성공할 경우 세션에 로그인 여부값을 저장한다.
            request.session['login_chk'] = True
            request.session['login_user_idx'] = user_model.user_idx

            r1 = '''
                <script>
                    alert('로그인에 성공하였습니다')
                    location.href = '/'
                </script>
                '''
        # 비밀번호가 다를 경우
        else :
            r1 = '''
                <script>
                    alert('비밀번호가 잘못되었습니다')
                    location.href = '/user/login?login_chk=1'
                </script>
                 '''
    except :
        # 아이디가 없을 경우
        r1 = '''
            <script>
                alert('존재하지 않는 아이디 입니다')
                location.href = '/user/login?login_chk=1'
            </script>
             '''

    return HttpResponse(r1)


# /user/logout
def logout(request) :
    # 세션 영역에 저장되어 있는 로그인 값을 삭제한다.
    del request.session['login_chk']
    del request.session['login_user_idx']

    r1 = '''
        <script>
            alert('로그아웃 되었습니다')
            location.href = '/'
        </script>
         '''

    return HttpResponse(r1)


# /user/modify_user_result
@csrf_exempt
def modify_user_result(request) :
    # 파라미터 데이터
    user_pw = request.POST['user_pw']
    # 로그인한 사용자 번호
    login_user_idx = request.session['login_user_idx']

    # 로그인한 사용자 정보를 가져온다.
    login_user_model = user_app.models.UserTable.objects.get(user_idx=login_user_idx)
    # 새로운 정보를 셋팅한다.
    login_user_model.user_pw = user_pw
    # 저장한다.
    login_user_model.save()

    r1 = '''
        <script>
            alert('수정되었습니다')
            location.href = '/user/modify_user'
        </script>
         '''
    return HttpResponse(r1)

