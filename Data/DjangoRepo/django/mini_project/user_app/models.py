from django.db import models

# Create your models here.
# 사용자 정보 테이블
class UserTable(models.Model) :
    # PK 컬럼(1부터 1씩 증가되는 값으로 저장된다.)
    user_idx = models.AutoField(primary_key=True)
    # varchar(50), not null
    user_name = models.CharField(max_length=50)
    # varchar(100), unique, not null
    user_id = models.CharField(max_length=100, unique=True)
    # varchar(100), not null
    user_pw = models.CharField(max_length=100)