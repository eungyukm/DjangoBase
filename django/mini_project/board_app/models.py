from django.db import models
from user_app.models import UserTable

# Create your models here.

# 게시판 정보 테이블
class BoardInfoTable(models.Model) : 
    board_info_idx = models.AutoField(primary_key=True)
    board_info_name = models.CharField(max_length=500)

# 게시글 정보 테이들
class ContentTable(models.Model) :
    content_idx = models.AutoField(primary_key=True)
    content_subject = models.CharField(max_length=500)
    content_text = models.TextField()
    # upload_to : settings.py 파일에 설정한 업로드 폴더 하위에
    # 
    content_file = models.FileField(upload_to='files/', null=True)
    # 외래키(UserTable의 PK 컬럼을 참조합니다.
    # 만약 참조하는 테이블의 PK 컬럼이 아닌 다른 컬럼을 참조하겠다면
    # related_name='컬럼명'을 설정해 줍니다.
    content_writer_idx = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    # 외래키(BoardInfoTable의 PK 컬럼을 참조한다)
    content_board_idx = models.ForeignKey(BoardInfoTable, on_delete=models.CASCADE)
    content_date = models.DateTimeField()