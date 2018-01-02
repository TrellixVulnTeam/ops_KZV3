#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models



TASK_TYPE = (
    # (str(1), u"数据库"),
    (str(2), u"gitlab"),
    (str(3), u"申请发布"),
    (str(4), u"申请主机"),
    (str(5), u"其他")
    )
TOOL_RUN_TYPE = (
    (0, 'shell'),
    (1, 'python'),
    (2, 'sql'),
)

class Task(models.Model):
    tool_script = models.TextField(verbose_name='脚本', null=True, blank=True)
    tool_run_type = models.IntegerField(choices=TOOL_RUN_TYPE, verbose_name='脚本类型', default=0)
    task_name = models.CharField(u"任务名称", max_length=30, null=True)
    task_type = models.CharField(u"任务类型", max_length=30, null=True)
    task_desc = models.CharField(u"任务描述", max_length=256, null=True)
    task_applyer_name = models.CharField(u"申请人", max_length=30, null=True)
    task_approve_name = models.CharField(u"审批人", max_length=30, null=True)
    task_executer = models.CharField(u"执行人", max_length=30, null=True)
    apply_time = models.CharField(u"提交时间", max_length=30, null=True)
    finish_time = models.CharField(u"完成时间", max_length=30, null=True)
    is_finished = models.CharField(u"完成时间", max_length=30, null=True)
    task_script_path = models.CharField(max_length=100, blank=True, null=True, verbose_name='脚本路径', default=None)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'任务中心'
        verbose_name_plural = verbose_name
class File(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='%Y-%m-%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FileSimpleModel(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
    file_field = models.FileField(upload_to="upload/%Y-%m-%d")
