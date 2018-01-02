#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from users.models import *

class RoleListForm(forms.ModelForm):
    class Meta:
        model = RoleList
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permission': forms.SelectMultiple(attrs={'class': 'form-control', 'size':'10', 'multiple': 'multiple'}),
        }

    def __init__(self,*args,**kwargs):
        super(RoleListForm,self).__init__(*args, **kwargs)
        self.fields['name'].label = u'名 称'
        self.fields['name'].error_messages = {'required': u'请输入名称'}
        # self.fields['permission'].label = u'URL'
        # self.fields['permission'].required = False

class UserGroupModelForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('username', 'password', 'name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username@zofund.com'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
