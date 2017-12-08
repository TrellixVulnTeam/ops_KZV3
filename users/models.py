from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'角色')
    comment = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name_plural = u'角色表'
        # db_table = 't_role'


class UserGroup(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'组名')
    comment = models.CharField(max_length=160, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=u'创建时间')
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'用户组'
        # db_table = 't_usergroup'


# todo:扩展django user模型
class User(AbstractUser):
    # id = models.AutoField(primary_key=True)
    USER_ROLE_CHOICES = (
        ('SU', u'超级管理员'),
        ('GA', u'组管理员'),
        ('CU', u'2普通用户')
    )
    name = models.CharField(max_length=100, verbose_name='', null=True)
    avatar = models.CharField(max_length=255, verbose_name=u'头像', null=True, blank=True)
    group = models.ManyToManyField(UserGroup)

    class Meta:
        managed = True
        verbose_name_plural = u'用户表'
        # db_table = 't_user'
