from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import script
import json
from .form import ToolForm
from users.models import User





@login_required
def tools(request):
    obj = script.objects.all()
    user_list = User.objects.all()
    for q in user_list:
        login_user = request.user.username
        if q.username == login_user:
            if q.level == '1':
                return render(request, "mysql/tools.html",
                              {"tools": obj, "tasks_active": "active", "tools_active": "active"})
        else:
                return render(request, "mysql/tools-normal.html",
                              {"tools": obj, "tasks_active": "active", "tools_active": "active"})

@login_required
def tools_add(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            user = request.user.username
            tools_save = form.save()
            # applyer_name = request.user.username
            # Script = script(applyer_name=applyer_name)
            # Script.save()
            form = ToolForm()
            return render(request, 'mysql/tools-add.html',
                          {'form': form, "tasks_active": "active", "tools_active": "active",
                           "msg": "添加成功"})
    else:
        form = ToolForm()
    return render(request, 'mysql/tools-add.html',
                  {'form': form, "tasks_active": "active", "tools_active": "active", })


@login_required
def tools_update(request, nid):
    tool_id = get_object_or_404(script, id=nid)

    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool_id)
        if form.is_valid():
            asset_save = form.save()
            return redirect('tools.html')

    form = ToolForm(instance=tool_id)
    return render(request, 'mysql/tools-update.html',
                  {'form': form, 'nid': nid, "tasks_active": "active", "tools_active": "active", })


@login_required
def tools_delete(request):
    ret = {'status': True, 'error': None, }
    if request.method == "POST":
        try:
            id_1 = request.POST.get("nid", None)
            script.objects.get(id=id_1).delete()
        except Exception as e:
            ret['status'] = False
            ret['error'] = '删除请求错误,{}'.format(e)
        return HttpResponse(json.dumps(ret))


# @login_required
# def tools_bulk_delte(request):
#     ret = {'status': True, 'error': None, }
#     if request.method == "POST":
#         try:
#             ids = request.POST.getlist('id', None)
#             idstring = ','.join(ids)
#             script.objects.extra(where=['id IN (' + idstring + ')']).delete()
#         except Exception as e:
#             ret['status'] = False
#             ret['error'] = '删除请求错误,{}'.format(e)
#         return HttpResponse(json.dumps(ret))



@login_required()
def scripts_success(request):
    """
       审批通过任务
       :param request:
       :return:
       """
    # task_all = Task.objects.all()
    ret = {'status': '', 'Message': ''}
    if request.method == 'POST':
        ids = request.POST.get("nid", None)
        if script.objects.get(id=ids).is_finished == '1':
            ret['status'] = 0
            ret['message'] = '该任务已审批'
        else:
            is_finished = 1
            script.objects.filter(id=ids).update(is_finished=is_finished)
            ret['status'] = 1
            ret['message'] = '执行成功'
    return HttpResponse(json.dumps(ret))








