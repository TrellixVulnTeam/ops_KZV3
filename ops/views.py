#!/usr/bin/env python
# encoding: utf-8

import psutil
import platform
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
# 权限认证模块
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.core.urlresolvers import reverse
from users.models import User



def init(request):
    """
    初始化系统
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 清空不必要数据
        User.objects.all().delete()
        # Asset.objects.all().delete()

        # 初始化数据
        user = User(username='admin', password='admin', name='weirongguo', email='weirongguo@candaochina.com')
        # user = User(username='test', password='test', name='test', email='test@candaochina.com')
        user.set_password(user.password)
        user.save()

        return HttpResponse(u'初始化系统成功')
    else:
        return render(request, 'setup.html', locals())


def index(request):
    """
    defautl page
    :param request:
    :return:
    """
    # return render_to_response('dashboard.html')
    return HttpResponseRedirect(reverse(dashboard))


@login_required()
def lockscreen(request):
    """
    lockscreen page
    :param request:
    :return:
    """
    if request.method == 'POST':
        pass
    else:
        return render_to_response('lockscreen.html')


def Login(request):
    """
    登录页面
    此处会用到系统login方法,防止重名,所以使用大写开头
    :param request:
    :return:
    """
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse(dashboard))
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        post_check_code = request.POST.get('captcha')
        session_check_code = request.session['check_code']

        if post_check_code.lower() == session_check_code.lower():
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.session['session_user_id'] = {'user': username}
                        # return HttpResponseRedirect(reverse(dashboard))
                        return HttpResponseRedirect(request.POST.get('next', '/'))
                    else:
                        error = '用户未激活'
                else:
                    error = '用户名或密码错误'
        else:
            error = '验证码错误'
        return render_to_response('login.html', {'error': error})
    else:
        next = request.GET.get('next', '/')
        # return render_to_response('login.html', locals())
        return render(request, 'login.html', locals())


@login_required()
def dashboard(request):
    """
    首页仪表盘
    :param request:
    :return:
    """
    # asset_count = Asset.objects.count()
    # project_count = Project.objects.count()

    server_info = {}
    header_title, sub_title = "我的服务资源", ""
    # header_title, path1, path2 = '仪表盘', '12346', '789'
    server_info['hostname'] = platform.node()
    server_info['system_info'] = '%s,%s,%s' % (
        platform.system(), ' '.join(platform.linux_distribution()), platform.release())
    server_info['arch'] = ' '.join(platform.architecture())
    server_info['procesor'] = platform.processor()
    server_info['py_version'] = platform.python_version()
    # //是向下取整除法
    server_info['total_mem'] = psutil.virtual_memory().total / 1024 // 1024

    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    green, orange, red, grey = '#00FF38', '#FFB400', '#FF3B00', '#EBEBEB'

    ram_color = green
    if ram >= 75:
        ram_color = red
    elif ram >= 50:
        ram_color = orange

    cpu_color = green
    if cpu >= 75:
        cpu_color = red
    elif cpu >= 50:
        cpu_color = orange

    server_info['cpu_idel'] = 100 - cpu
    server_info['cpu_color'] = cpu_color
    server_info['cpu'] = cpu
    server_info['ram'] = 100 - ram
    server_info['ram_used'] = ram
    server_info['ram_color'] = ram_color
    # return render_to_response('dashboard.html',locals())
    return render(request, 'dashboard.html', locals())


@login_required()
def setting(request):
    header_title, sub_title, path1, path2 = "", "", "设置", ""
    return render(request, 'setting.html', locals())

#
# @login_required()
# def web_terminal(request):
#     host_id = request.GET.get('instance_id', None)
#     zone = request.GET.get('zone', None)
#     asset = Asset.objects.get(id=host_id)
#     if asset:
#         hostname = asset.hostname
#     return render(request, 'web_terminal.html', locals())


def Logout(request):
    """
    退出系统
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse(dashboard))


def page404(request):
    """
    404 page
    :param request:
    :return:
    """
    return render_to_response('404.html')


def page500(request):
    """
    500 page
    :param request:
    :return:
    """
    return render_to_response('500.html')


def help(request):
    return render_to_response('help.html')
