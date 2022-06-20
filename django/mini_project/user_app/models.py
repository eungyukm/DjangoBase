from django.db import models

# Create your models here.
# 사용자 정보 테이블
class UserTable(models.Model) :
    # PK 컬럼(1부터 1씩 증가되는 값으로 저장됩니다.)
    user_idx = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=100, unique=True)
    user_pw = models.CharField(max_length=100)