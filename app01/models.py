from django.db import models

# Create your models here.
class DreamReal(models.Model):  # 创建一个模型也就是实体
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumber = models.IntegerField

    class Meta: # 元类
        db_table = 'dreamreal'
