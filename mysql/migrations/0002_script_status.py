# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-09 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]