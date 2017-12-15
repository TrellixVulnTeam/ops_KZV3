#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^role/add/$', role_add, name='role_add'),
    url(r'^role/list/$', role_list, name='role_list'),
    url(r'^role/edit/(?P<ids>\d+)/$', role_edit, name='role_edit'),
    url(r'^role/delete/(?P<ids>\d+)/$', role_del, name='role_del'),

    url(r'^group$', group_list, name='user_group_list'),
    url(r'^group/detail$', group_detail, name='user_group_detail'),
    url(r'^group/get_list$', get_grouplist, name='user_group_getlist'),
    url(r'^group/create$', group_create, name='user_group_add'),
    url(r'^group/edit$', group_edit, name='user_group_edit'),
    url(r'^group/del$', group_del, name='user_group_del'),

    url(r'^user$', user_list, name='user_list'),
    url(r'^user/captcha/$', captcha, name='captcha'),
    url(r'^user/get_list/$', get_userlist, name='user_getlist'),
    url(r'^user/create/$', user_create, name='user_add'),
    url(r'^user/edit/$', user_edit, name='user_edit'),
    url(r'^user/del/$', user_del, name='user_del'),
    # url(r'^user/del/(?P<ids>\d+)/$', user_del, name='user_del'),
    url(r'user/detail/$', user_detail, name='user_detail'),
    url(r'^user/profile/$', user_profile, name='user_profile'),

    url(r'^password/forget/$', forget_password, name='password_forget'),
    url(r'^password/reset/$', reset_password, name='password_reset'),
]
