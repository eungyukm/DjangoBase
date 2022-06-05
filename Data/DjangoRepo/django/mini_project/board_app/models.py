from django.db import models
from user_app.models import UserTable

# Create your models here.

# 게시판 정보 테이블
class BoardInfoTable(models.Model) :
    # primary key, auto increment
    board_info_idx = models.AutoField(primary_key=True)
    # varchar(500), not null
    board_info_name = models.CharField(max_length=500)


# 게시글 정보 테이블
class ContentTable(models.Model) :
    # primary key, auto increment
    content_idx = models.AutoField(primary_key=True)
    # varchar(500), not null
    content_subject = models.CharField(max_length=500)
    # 장문 문자열, not null
    content_text = models.TextField()
    # varchar(500), null
    # upload_to : settings.py 파일에 설정한 업로드 폴더 하위에
    # 생성될 폴더이름. 여기에 파일이 업로드 된다.
    content_file = models.FileField(upload_to='files/', null=True)
    # 외래키(UserTable의 PK 컬럼을 참조한다.), not null
    # 만약 참조하는 테이블의 PK 컬럼이 아닌 다른 컬럼을 참조하게 하겠다면
    # related_name='컬럼명' 을 설정해준다.
    content_writer_idx = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    # 외래키(BoardInfoTable의 PK 컬럼을 참조한다), not null
    content_board_idx = models.ForeignKey(BoardInfoTable, on_delete=models.CASCADE)
    # 날짜, not null
    content_date = models.DateTimeField()
