from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class RoleLevel(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'角色')
    role_level = models.CharField(max_length=160, blank=True, null=True, verbose_name=u'角色等级')

    def __unicode__(self):
        return self.name
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

class RoleList(models.Model):
    name = models.CharField(max_length=64)
    # permission = models.ManyToManyField(PermissionList, null=True, blank=True)


    def __unicode__(self):
        return self.name
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
    # role = models.ManyToManyField(Role)
    level = models.CharField(max_length=100, verbose_name='', null=True)
    role = models.ForeignKey(RoleList, null=True, blank=True)

    class Meta:
        managed = True
        verbose_name_plural = u'用户表'
        # db_table = 't_user'
