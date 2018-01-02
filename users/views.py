from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
import json
import datetime
import io
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from users.forms import *
from ops.common import *
from users.models import RoleList
from users.forms import RoleListForm
from django.contrib.auth import get_user_model

# Create your views here.

@login_required
def role_add(request):
    header_title, sub_title, path1, path2 = "", "", "用户管理", "角色添加"
    temp_name = "accounts/accounts-header.html"
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('role_list'))
    else:
        form = RoleListForm()

    kwvars = {
        'temp_name': temp_name,
        'form': form,
        'request': request,
    }

    return render(request, 'users/role_add.html', locals())


@login_required
def role_list(request):
    header_title, sub_title, path1, path2 = "", "", "用户管理", "角色列表"
    temp_name = "accounts/accounts-header.html"
    all_role = RoleList.objects.all()
    return render(request, 'users/role_list.html', locals())


@login_required
def role_edit(request, ids):
    header_title, sub_title, path1, path2 = "", "", "用户管理", "角色编辑"
    iRole = RoleList.objects.get(id=ids)
    temp_name = "accounts/accounts-header.html"
    if request.method == "POST":
        form = RoleListForm(request.POST, instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('role_list'))
    else:
        form = RoleListForm(instance=iRole)

    kwvars = {
        'temp_name': temp_name,
        'ids': ids,
        'form': form,
        'request': request,
    }

    return render(request, 'users/role_edit.html', locals())


@login_required
def role_del(request, ids):
    RoleList.objects.filter(id=ids).delete()
    return HttpResponseRedirect(reverse('role_list'))


@login_required()
def group_list(request):
    """
    组列表
    :param request: 
    :return: 
    """
    header_title, sub_title, path1, path2 = "", "", "用户管理", "用户组列表"
    # return render_to_response('user/group_list.html', locals())
    return render(request, 'users/group_list.html', locals())



@login_required()
def get_grouplist(request):
    """
    
    :param request: 
    :return: 
    """
    offset = request.GET.get('offset', None)
    limit = request.GET.get('limit', None)
    sort = request.GET.get('sort', None)
    keywords = request.GET.get('search', None)
    if sort is None:
        sort = "name"
    order = request.GET.get('order', None)
    if order == "desc":
        sort = "-name"
    count = UserGroup.objects.all().count()
    # group_list = UserGroup.objects.all()[int(offset):int(offset + limit)]
    group_list = UserGroup.objects.order_by(sort).all()[int(offset):int(offset + limit)]
    if keywords:
        group_list = UserGroup.objects.order_by(sort).filter(
            Q(name__icontains=keywords) | Q(comment__icontains=keywords))[int(offset):int(offset + limit)]
    rows = [
        {
            'id': g.id,
            'name': g.name,
            'comment': g.comment,
            'usernumber': g.user_set.count()
        } for g in group_list]
    data = {'total': count, 'rows': rows}
    return JsonResponse(data)


@login_required()
def group_create(request):
    """
    添加组
    :param request: 
    :return: 
    """
    user_all = User.objects.all()

    if request.method == 'POST':
        group_form = UserGroupModelForm(request.POST)
        ret = {'code': 0, 'message': ''}

        if group_form.is_valid():
            name = group_form.cleaned_data['name']
            comment = group_form.cleaned_data['comment']
            # name = request.POST.get('name', '')
            # comment = request.POST.get('comment', '')
            user_select = request.POST.getlist('users_selected', [])

            if UserGroup.objects.filter(name=name):
                ret['code'] = 0
                ret['message'] = '组名已经存在'
            else:
                # obj = UserGroup.objects.create(name=name, comment=comment)
                group = UserGroup.objects.filter(name=name)
                if not group:
                    # 插入组记录
                    group = UserGroup(name=name, comment=comment)
                    group.save()
                    # 把选择的用户添加到这个组
                    for user_id in user_select:
                        user = User.objects.get(id=user_id)
                        group.user_set.add(user)
                    ret['code'] = 1
            return HttpResponse(json.dumps(ret))
        else:
            ret['code'] = 0
            ret['message'] = '执行失败'
            return HttpResponse(json.dumps(ret))
    else:
        group_form = UserGroupModelForm()
        return render_to_response('users/group_add.html', locals())


@login_required()
def group_edit(request):
    """
    修改组
    :param request: 
    :return: 
    """
    group_id = request.GET.get('id', None)
    group = UserGroup.objects.get(id=group_id)
    user_all = User.objects.all()
    users_selected = User.objects.filter(group=group)
    users_no_selected = User.objects.filter(~Q(group=group))
    ret = {'code': 0, 'message': ''}

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        users_selected = request.POST.getlist('users_selected')
        group_form = UserGroupModelForm(request.POST)
        if group_form.is_valid():
            # data = form.cleaned_data
            # group.name = data['name']
            # group.comment = data['comment']
            # if len(UserGroup.objects.filter(name=data['name'])) > 1:
            #    ret['code'] = 0
            #    ret['message'] = 'failed'
            # else:
            #    group.save()
            #    ret['code'] = 1
            group.user_set.clear()
            group = UserGroup.objects.get(id=group_id)
            for user_id in users_selected:
                user = User.objects.get(id=user_id)
                group.user_set.add(user)
            UserGroup.objects.filter(id=group_id).update(name=name, comment=comment)
            ret['code'] = 1
            return HttpResponse(json.dumps(ret))
        else:
            ret['code'] = 0
            ret['message'] = '编辑失败，请检查！'
            return HttpResponse(json.dumps(ret))
    else:
        group_form = UserGroupModelForm(instance=group)
        return render_to_response('users/group_edit.html', locals())


@login_required()
def group_del(request):
    """
    删除组
    :param request: 
    :return: 
    """
    ret = {'code': 0, 'message': ''}
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')
        for id in ids:
            UserGroup.objects.get(id=id).delete()
            ret['code'] = 1
            ret['message'] = '执行成功'
    return HttpResponse(json.dumps(ret))


@login_required()
def group_detail(request):
    header_title, sub_title, path1, path2 = "", "", "用户管理", "用户组详情"
    group_id = request.GET.get('id', None)
    user_group = UserGroup.objects.get(id=group_id)
    users_selected = User.objects.filter(group=user_group)
    users_no_selected = User.objects.filter(~Q(group=user_group))
    return render(request, 'users/group_detail.html', locals())


@login_required()
def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    header_title, sub_title, path1, path2 = "", "", "用户", "用户列表"
    # return render_to_response('user/user_list.html', locals())
    return render(request, 'users/user_list.html', locals())
# @login_required()
# def user_list(request):
#     header_title, sub_title, path1, path2 = "", "", "用户", "用户列表"
#     all_user = get_user_model().objects.all()
#     kwargs = {
#         # 'temp_name': temp_name,
#         'all_user':  all_user,
#     }
#     return render(request, 'users/user_list.html', locals())

# 用户组转为字符串
# def groups2str(group_list):
#     """
#     将用户组列表转换为str
#     """
#     if len(group_list) < 3:
#         return ' '.join([group.name for group in group_list])
#     else:
#         return '%s ...' % ' '.join([group.name for group in group_list[0:2]])


@login_required()
def get_userlist(request):
    """
    获取用户列表，返回json
    :param request: 
    :return: 
    """
    # todo:两种json用法
    # 官方示例格式 test ok
    # data = {'total': 79, 'rows': [{'id': 1, 'username': 'tom', 'email': 'tom@123.com'},
    #                              {'id': 2, 'username': 'jerry', 'email': 'jerry@123.com'},
    #                              {'id': 3, 'username': 'lucy', 'email': 'lucy@123.com'}]}
    # return HttpResponse(json.dumps(data))
    # return JsonResponse(data)
    # end

    offset = request.GET.get('offset', None)
    limit = request.GET.get('limit', None)
    sort = request.GET.get('sort', None)
    keywords = request.GET.get('search', None)

    if sort is None:
        sort = "username"

    order = request.GET.get('order', None)
    if order == "desc":
        sort = "-username"

    gid = request.GET.get('uid', None)
    if gid:
        user_group = UserGroup.objects.filter(id=gid)

        if user_group:
            print(user_group)
            user_group = user_group[0]
            user_list = user_group.user_set.all()

    count = User.objects.all().count()
    # user_list = User.objects.all()
    user_list = User.objects.order_by(sort).all()[int(offset):int(offset + limit)]
    if keywords:
        # TODO:搜索多个字段
        user_list = User.objects.order_by(sort).filter(Q(username__icontains=keywords) | Q(name__icontains=keywords))[
                    int(offset):int(offset + limit)]
    # if (type(sort) != 'NoneType') and (order == 'asc'):
    #     user_list = User.objects.all()[int(offset):int(offset + limit)].order_by(sort)
    # else:
    #    user_list = User.objects.all()[int(offset):int(offset + limit)].order_by('-' + sort)
    if gid:
        print(gid)
    rows = [
        {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            # 'group': groups2str(user.group.all()),
            'group': object2str(user.group.all()),
            'role': user.role_id,
            'is_active': user.is_active,
        } for user in user_list]
    data = {'total': count, 'rows': rows}
    return JsonResponse(data)
    # return HttpResponse(json.dumps(data))


def captcha(request):
    """
    captcha
    :param request: 
    :return: 
    """
    stream = io.BytesIO()
    image, code = captcha2()
    image.save(stream, 'png')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())


@login_required()
def user_create(request):
    """
    添加用户
    :param request: 
    :return: 
    """
    header_title, sub_title, path1, path2 = "", "", "用户", "添加用户"
    # u1 = User.objects.get(id=1)
    # r1 = Role.objects.get(id=2)
    # # 多对多添加数据方式(2种方式)
    # r1.user_set.add(u1)
    # # u1.role_relation.add(r1)
    # role_level = {'dev': u'开发工程师', 'test': u'测试工程师', 'ops': u'运维工程师', 'leader': u'组长'}
    user_role = {'SU': u'超级管理员', 'CU': u'普通用户'}
    group_all = UserGroup.objects.all()
    roles_all = RoleList.objects.all()

    if request.method == 'POST':
        # username = request.POST.get('username', None)
        # passwrod = request.POST.get('password', None)
        user_form = UserModelForm(request.POST)
        ret = {'code': 0, 'message': ''}
        # TODO:获取表单错误信息
        print(user_form.errors)
        # data = user_form.cleaned_data
        # username = data['username']
        # print(username)
        username = request.POST.get('username', '')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        groups = request.POST.getlist('groups', [])
        right = request.POST.get('right', 'CU')
        role_id = request.POST.get('role', '')
        print(role_id)
        ssh_key_pwd = ''
        is_active = True
        level = '0'
        # role = ''.join(role)
        user = User(username=username, name=name, password=password, email=email, is_active=is_active,
                    date_joined=datetime.datetime.now(), role_id=role_id, level=level)
        user.set_password(password)
        user.save()
        # if role:
        #     roles_select = []
        #     for role_id in role:
        #         roles_select.extend(RoleList.objects.filter(id=role_id))
        #     user.role = roles_select
        if groups:
            group_select = []
            for group_id in groups:
                group_select.extend(UserGroup.objects.filter(id=group_id))
            user.group = group_select

        # user_form.save()
        # user_form.save_m2m()
        return HttpResponseRedirect(reverse(user_list))
    else:
        user_form = UserModelForm()
        # return render_to_response('user/user_add.html', locals())
        return render(request, 'users/user_add.html', locals())


@login_required()
def user_edit(request):
    """
    编辑用户
    :param request: 
    :return: 
    """
    header_title, sub_title, path1, path2 = "", "", "用户", "编辑用户"
    user_id = request.GET.get('id', None)
    group_all = UserGroup.objects.all()
    roles_all = RoleList.objects.all()
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        # TODO:获取表单错误信息
        # print(form.errors)
        print(form.errors.as_json())
        if user_id:
            user = User.objects.filter(id=user_id)
            username = request.POST.get('username', None)
            name = request.POST.get('name', None)
            password = request.POST.get('password', None)
            email = request.POST.get('email', None)
            groups = request.POST.getlist('groups', [])
            role_id = request.POST.get('role', None)
            if user:
                user.update(username=username, name=name, email=email, role_id=role_id)
                if password:
                    user_get = user[0]
                    user_get.set_password(password)
                    user_get.save()
                if groups:
                    user_get = user[0]
                    user_get.group.clear()
                    group_select = []
                    for group_id in groups:
                        group_select.extend(UserGroup.objects.filter(id=group_id))
                    user_get.group = group_select
            return HttpResponseRedirect(reverse(user_list))
    else:
        user = User.objects.get(id=user_id)
        user_form = UserModelForm(instance=user)
        groups_str = ' '.join([str(group.id) for group in user.group.all()])
        rolelist = RoleList.objects.all()
        return render(request, 'users/user_edit.html', locals())


@login_required()
def user_del(request):
    """
    删除用户
    :param request: 
    :return: 
    """
    ret = {'Code': 0, 'Message': ''}
    if request.method == 'POST':
        # for key in request.POST:
        #     print(key)
        #     valuelist = request.POST.getlist(key)
        #     print(valuelist)
        ids = request.POST.getlist('ids[]')
        for id in ids:
            if User.objects.get(id=id).username == 'admin':
                ret['code'] = 0
                ret['message'] = '内置管理员不允许删除'
                continue
            else:
                User.objects.get(id=id).delete()
                ret['code'] = 1
                ret['message'] = '执行成功'
    return HttpResponse(json.dumps(ret))


@login_required()
def user_profile(request):
    return render(request, 'users/user_profile.html', locals())


@login_required()
def user_detail(request):
    return render(request, 'users/user_detail.html', locals())


def forget_password(request):
    return render(request, 'users/forget_password.html', locals())


@login_required()
def reset_password(request):
    return render(request, 'users/reset_password.html', locals())
