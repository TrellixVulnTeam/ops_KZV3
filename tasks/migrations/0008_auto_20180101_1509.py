# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-01 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20171228_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_desc',
            field=models.TextField(max_length=100, null=True, verbose_name='任务描述'),
        ),
    ]
