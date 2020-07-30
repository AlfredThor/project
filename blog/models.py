from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import  User


class Article(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='自增主键')
    title = models.CharField(verbose_name='文章标题',max_length=100)
    intro = models.CharField(max_length=300,verbose_name='文章简介')
    content = MDTextField(verbose_name='文章正文')
    time = models.DateField(verbose_name='发布时间')
    number = models.IntegerField(verbose_name='阅读量')
    sort = models.ForeignKey('Sort',to_field='id',on_delete=models.CASCADE,verbose_name='分类外键')
    user = models.ForeignKey(User,to_field='id', on_delete=models.CASCADE, related_name='profile',verbose_name='关联USER模型，一对一')

    class Mate:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def update_number(self):
        self.number += 1
        self.save(update_fields=['number'])

class Member(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='自增主键')
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='用户一对一外键')

    class Mate:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user

class Sort(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='自增主键')
    name = models.CharField(max_length=10,verbose_name='分类')

    class Mate:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Userip(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(verbose_name='IP地址', max_length=30)
    count = models.IntegerField(default=0,verbose_name='访问次数')
    time = models.DateField()

    class Mate:
        verbose_name = '访问统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip