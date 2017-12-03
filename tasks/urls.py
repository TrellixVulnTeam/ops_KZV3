#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url
from tasks.views import *
urlpatterns = [
    url(r'^task$', task_list, name='task_list'),
    url(r'^add/$', task_add, name='task_add'),
    url(r'^del/$', task_del, name='task_del'),
    url(r'^search/$', task_search, name='task_search'),
]