#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
import json
import datetime
import io
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from tasks.forms import *
from ops.common import *

@login_required()
def task_list(request):
    """
       组列表
       :param request:
       :return:
       """
    header_title, sub_title, path1, path2 = "", "", "任务系统", "任务管理"
    # return render_to_response('user/group_list.html', locals())
    return render(request, 'tasks/task_list.html', locals())




@login_required()
def task_add(request):
    """
       组列表
       :param request:
       :return:
       """
    header_title, sub_title, path1, path2 = "", "", "任务系统", "创建任务"
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        if task_form.is_valid():
            task_name = task_form.cleaned_data['task_name']
            if Task.objects.filter(name=task_name):
                pass
            else:
                task_form.save()
            return HttpResponseRedirect(reverse(task_list))
    else:
        task_form = TaskModelForm()
    return render(request, 'tasks/task_add.html', locals())





@login_required()
def task_del(request):
    """
       组列表
       :param request:
       :return:
       """
    header_title, sub_title, path1, path2 = "", "", "任务管理", "删除任务"
    ret = {'Code': 0, 'Message': ''}
    if request.method == 'POST':
        # for key in request.POST:
        #     print(key)
        #     valuelist = request.POST.getlist(key)
        #     print(valuelist)
        ret = {'code': 0, 'message': ''}
        if request.method == 'POST':
            ids = request.POST.getlist('ids[]')
            for id in ids:
                Task.objects.get(id=id).delete()
                ret['code'] = 1
                ret['message'] = '执行成功'
        return HttpResponse(json.dumps(ret))



@login_required()
def task_search(request):
    """
       组列表
       :param request:
       :return:
       """
    header_title, sub_title, path1, path2 = "", "", "任务管理", "查询任务"
    # return render_to_response('user/group_list.html', locals())
    return render(request, 'tasks/task_detail.html', locals())
