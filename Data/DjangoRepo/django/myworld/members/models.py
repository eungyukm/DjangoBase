from operator import mod
from django.db import models

# Create your models here.
# 테이블 구조와 동일한 구조의 class (model)을 정의한다.
class Members(models.Model) :
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)