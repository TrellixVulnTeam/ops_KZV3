#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url
from tasks.views import *
urlpatterns = [
    url(r'^task/$', task_list, name='task'),
    url(r'^task/add/$', task_add, name='task_add'),
    url(r'^task/search/$', task_search, name='task_search'),
    url(r'^task/getlist/$', get_tasklist, name='get_task_list'),
    url(r'^task/edit/$', task_edit, name='task_edit'),
    url(r'^task/edit/success$', task_success, name='task_success'),
    url(r'^task/detail/$', task_detail, name='task_detail'),
    url(r'^task/todo/$', task_todo, name='task_todo'),
    url(r'^task/myself/$', task_myself, name='task_myself'),
    # url(r'^task/add/fileupload/$', FileUpload.as_view(), name='FileUpload'),
    # url(r'^upload/$', upload_file, name='FileUploadForm'),
    # url(r'^clear/$', clear_database, name='clear_database'),


]