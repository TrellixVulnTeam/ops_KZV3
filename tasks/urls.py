#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url
from tasks.views import *
urlpatterns = [
    url(r'^task/$', task_list, name='task'),
    url(r'^task/add/$', task_add, name='task_add'),
    url(r'^task/del/$', task_del, name='task_del'),
    url(r'^task/search/$', task_search, name='task_search'),
    url(r'^task/getlist/$', get_tasklist, name='get_task_list'),
    url(r'^task/edit/$', task_edit, name='task_edit'),

]