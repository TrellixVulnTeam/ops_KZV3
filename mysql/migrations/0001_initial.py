# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-02 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('envr_type', models.IntegerField(choices=[(0, 'dev'), (1, 'test'), (2, 'stable'), (3, 'pre'), (4, 'prod')], default=0, verbose_name='环境类型')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='脚本名称')),
                ('tool_script', models.TextField(blank=True, null=True, verbose_name='脚本')),
                ('tool_run_type', models.IntegerField(choices=[(2, 'sql')], default=0, verbose_name='类型')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '脚本',
                'verbose_name_plural': '脚本',
                'db_table': 'script',
            },
        ),
    ]
