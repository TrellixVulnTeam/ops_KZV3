#!/usr/bin/env python
# coding: utf-8

"""
@version: ??
@author: rongguo
@license: Apache Licence 
@contact: rongo.wei@gmail.com
@software: PyCharm
@project: oms
@file: context_processors.py.py
@time: 17-4-25 下午3:51
"""

"""自定义模板"""


# from account.models import User


# 注意：这里只有一个参数 即 HttpRequest 对象或当前用户的其他信息
def custom_proc(request):
    # 获取登录用户ID  login(request, account)
    user_id = request.user.id

    info_dict = {
        'session_user_id': user_id,
        'message_count': 5,
        'notify_count': 6,
        'task_count': 7,
    }
    return info_dict
