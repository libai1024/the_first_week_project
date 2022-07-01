from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length= 8,verbose_name= "员工姓名")
    age = models.IntegerField(verbose_name= "年龄")
    tel = models.CharField(max_length= 11,verbose_name="电话")
    detail = models.CharField(max_length= 256,verbose_name="具体信息")

    class Meta:
        verbose_name = '员工'  # 模型名称(单数)
        verbose_name_plural = verbose_name  # 模型名称(复数)

    def __str__(self):
        return self.name + "-" + str(self.age) + "-"+ self.tel

class MyUser(models.Model):
    username = models.CharField(max_length=18,verbose_name="账号")
    pwd =models.CharField(max_length=18,verbose_name="密码")

    class Meta:
        verbose_name = '用户员工'  # 模型名称(单数)
        verbose_name_plural = verbose_name  # 模型名称(复数)

    def __str__(self):
        return self.username
