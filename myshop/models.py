from django.db import models


# Create your models here.
class User(models.Model):
    gender = (('male', '男'), ('female', '女'))

    name = models.CharField(max_length=120,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    tags = models.CharField(max_length=100)
    goods_name = models.CharField(max_length=20)
    good_price = models.FloatField()
    good_img_id = models.CharField(max_length=10)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.goods_name


