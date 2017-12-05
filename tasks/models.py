#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


TASK_TYPE = (
    (str(1), u"数据库"),
    (str(2), u"gitlab"),
    (str(3), u"申请发布"),
    (str(4), u"申请主机"),
    (str(5), u"其他")
    )


class Task(models.Model):
    task_name = models.CharField(u"任务名称", max_length=30, null=True)
    task_type = models.CharField(u"任务类型", max_length=30, null=True)
    task_desc = models.CharField(u"任务描述", max_length=100, null=True)
    task_applyer_name = models.CharField(u"申请人", max_length=30, null=True)
    task_approve_name = models.CharField(u"审批人", max_length=30, null=True)
    task_executer = models.CharField(u"执行人", max_length=30, null=True)
    apply_time = models.CharField(u"提交时间", max_length=30, null=True)
    finish_time = models.CharField(u"完成时间", max_length=30, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'任务中心'
        verbose_name_plural = verbose_name
